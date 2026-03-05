from flask import Blueprint, render_template, jsonify, current_app, request
from data.menu_data import menu_data
from supabase import create_client

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/')
def index():

    normal_list = menu_data.get('Normal', [])
    high_list = menu_data.get('High-End', [])
    hard_list = menu_data.get('Hard Mode', [])
   
    return render_template(
        "costumer/index.html",
        menu=menu_data,
        normal_items=normal_list,
        high_items=high_list,
        hard_items=hard_list)

@customer_bp.route('/menu')
def menu():

    active_tier = "all" 
    return render_template("costumer/menu.html", menu=menu_data, active_tier=active_tier)

@customer_bp.route('/api/menu')
def api_menu():
    return jsonify(menu_data)

@customer_bp.route('/reserve')
def reserve_selection():
    return render_template("costumer/reserve_selection.html")

@customer_bp.route('/reserve/tiers')
def reserve_tiers():
    return render_template("costumer/tier_selection.html", menu=menu_data)

def get_supabase():
    url = "https://vtsmhotqxtmwyhwznvlx.supabase.co"
    key = "sb_publishable_wRKY-pk8AO5GZUO7pC5vxg_fzWLTlMM"

    print(f"DEBUG: URL is {url}")
    print(f"DEBUG: Key starts with {key[:10]}")
    return create_client(url, key)

@customer_bp.route('/reserve/table-selection/<tier>')
def table_selection(tier):
    tier_info = menu_data.get(tier)
    
    supabase = get_supabase()
    
    response = supabase.table('tables').select("*").order('table_number').execute()
    db_tables = response.data
    
    # Hatiin ang tables base sa capacity (2pax vs 4pax)
    couples = [t for t in db_tables if t['capacity'] == 2]
    family = [t for t in db_tables if t['capacity'] == 4]
    
    return render_template(
        "costumer/table_selection.html", 
        tier=tier, 
        tier_info=tier_info,
        couples=couples,
        family=family
    )

@customer_bp.route('/reserve/details')
def reserve_details():
    tier = request.args.get('tier')
    table_id = request.args.get('table') 
    
    tier_info = menu_data.get(tier)
    
    return render_template("costumer/booking_form.html", 
                           tier=tier, 
                           table_id=table_id,
                           tier_info=tier_info)
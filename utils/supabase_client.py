from supabase import create_client, Client
import os

def get_supabase_client() -> Client:
    url = os.environ.get('SUPABASE_URL')
    key = os.environ.get('SUPABASE_KEY')
    return create_client(url, key)

supabase: Client = get_supabase_client()
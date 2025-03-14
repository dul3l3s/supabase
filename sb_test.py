import os
from supabase import create_client, Client

url: str = "https://sesseszqgmjrpozofxpr.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNlc3Nlc3pxZ21qcnBvem9meHByIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5ODc2MTAsImV4cCI6MjA1NzU2MzYxMH0.J6Jnz18o5h2ABJPEpYiEfRZT_C5xJODAU6gUYlA72t4"
supabase: Client = create_client(url, key)

response = (
    supabase.table("produce")
    .select("*")
    .execute()
)

print(response)
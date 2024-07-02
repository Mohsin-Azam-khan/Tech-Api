import streamlit as st
import requests

st.title('Lead Submission Form')

# Input fields
lead_token = st.text_input("Lead Token", "36cc6d931fb14c44804c6830908b8def")
caller_id = st.text_input("Caller ID", "+17194451111")
traffic_source_id = st.text_input("Traffic Source ID", "1029")
first_name = st.text_input("First Name", "John")
last_name = st.text_input("Last Name", "Smith")
email = st.text_input("Email", "first-and-last-name@gmail.com")
address = st.text_input("Address", "123 Fake Street")
address2 = st.text_input("Address2", "Example")
city = st.text_input("City", "Boulder")
state = st.selectbox("State", [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID",
    "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO",
    "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
    "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
])
zip_code = st.text_input("Zip Code", "80301")
alternate_phone = st.text_input("Alternate Phone", "7890123456")
dob = st.date_input("Date of Birth")
marital_status = st.selectbox("Marital Status", ["single", "widowed", "separated", "divorced", "married"])
employment_status = st.selectbox("Employment Status", ["employed", "self_employed", "unemployed", "homemaker", "retired", "disabled", "separated"])
gender = st.selectbox("Gender", ["M", "F"])
spoken_language = st.selectbox("Spoken Language", ["English", "Spanish", "Chinese", "Tagalog", "Vietnamese", "French", "Arabic", "Korean", "Russian", "German"])
best_time_to_contact = st.selectbox("Best Time to Contact", ["anytime", "morning", "afternoon", "evening"])
sub_id = st.text_input("Sub ID", "sub123")
s1 = st.text_input("Sub ID 1", "subid1")
s2 = st.text_input("Sub ID 2", "subid2")
s3 = st.text_input("Sub ID 3", "subid3")
s4 = st.text_input("Sub ID 4", "subid4")
s5 = st.text_input("Sub ID 5", "subid5")
lead_type = st.text_input("Lead Type", "Exclusive")
original_lead_submit_date = st.text_input("Original Lead Submit Date", "2024-07-02 15:51:24")
ip_address = st.text_input("IP Address", "192.168.1.1")
source_url = st.text_input("Source URL", "http://example.com")
traffic_source_lead_id = st.text_input("Traffic Source Lead ID", "lead123")
aged_data = st.selectbox("Aged Data", [True, False])
jornaya_leadid = st.text_input("Jornaya Lead ID", "jornaya123")
trusted_form_cert_url = st.text_input("Trusted Form Cert URL", "http://example.com/trustedform")
tcpa_opt_in = st.selectbox("TCPA Opt In", [True, False])
tcpa_optin_consent_language = st.text_input("TCPA Opt In Consent Language", "I agree to the terms and conditions.")
payment_method_available = st.selectbox("Payment Method Available", [True, False])
monthly_affordable_payment_amount = st.number_input("Monthly Affordable Payment Amount", value=500)
jornaya_lead_id_agent = st.text_input("Jornaya Lead ID Agent", "jornaya_agent123")
trusted_form_cert_url_agent = st.text_input("Trusted Form Cert URL Agent", "http://example.com/trustedform_agent")
traffic_source_data_list_id = st.text_input("Traffic Source Data List ID", "list123")
traffic_source_agent_id = st.text_input("Traffic Source Agent ID", "agent123")
traffic_source_agent_name = st.text_input("Traffic Source Agent Name", "Agent Name")
traffic_source_agent_recording_url = st.text_input("Traffic Source Agent Recording URL", "http://example.com/recording")
ea_disposition = st.text_input("EA Disposition", "completed")
media_type = st.selectbox("Media Type", ["Google Ads", "Facebook Lead Ads", "Twitter", "TikTok", "YouTube", "Instagram", "SnapChat"])
traffic_source_platform = st.selectbox("Traffic Source Platform", ["TrackDrive", "Call Box", "Call Fire", "Call Rail", "Call Source", "Call Tracking Metrics", "Convirza", "Convoso", "Invoca", "Marchex", "Phonexa", "Retreaver", "Ringba", "ViciDial", "Vonage"])
blueink_secured_leads_token = st.text_input("Blue Ink Secured Leads Token", "968908503466600")
voluum_cid = st.text_input("Voluum CID", "voluum123")
gclid = st.text_input("Google Click ID", "gclid123")
fbeventid = st.text_input("Facebook Event ID", "fbevent123")
msclkid = st.text_input("Microsoft Click ID", "msclkid123")
useragent = st.text_input("User Agent", "Mozilla/5.0")
retreaver_call_uuid = st.text_input("Retreaver Call UUID", "retreaver_uuid123")
retreaver_call_key = st.text_input("Retreaver Call Key", "retreaver_key123")
ringba_call_uuid = st.text_input("Ringba Call UUID", "ringba_uuid123")
has_ssi = st.selectbox("Has SSI", [True, False])
has_medicaid = st.selectbox("Has Medicaid", [True, False])
has_copay = st.selectbox("Has Copay", [True, False])
has_government_benefits = st.selectbox("Government Benefits", [True, False])
medicare_parts_a_b = st.selectbox("Medicare Parts A&B", [True, False])
medicare_advantage_supplement = st.selectbox("Medicare Advantage or Supplement", ["advantage", "supplement", "unknown"])
permissiontrust_token = st.text_input("PermissionTrust Token", "permissiontrust123")

# When the user clicks the Submit button, send the POST request
if st.button('Submit'):
    url = "https://maas-media-tech-llc.trackdrive.com/api/v1/leads"
    data = {
        "lead_token": lead_token,
        "caller_id": caller_id,
        "traffic_source_id": traffic_source_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "address": address,
        "address2": address2,
        "city": city,
        "state": state,
        "zip": zip_code,
        "alternate_phone": alternate_phone,
        "dob": dob.strftime("%Y-%m-%d"),
        "marital_status": marital_status,
        "employment_status": employment_status,
        "gender": gender,
        "spoken_language": spoken_language,
        "best_time_to_contact": best_time_to_contact,
        "sub_id": sub_id,
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "s4": s4,
        "s5": s5,
        "lead_type": lead_type,
        "original_lead_submit_date": original_lead_submit_date,
        "ip_address": ip_address,
        "source_url": source_url,
        "traffic_source_lead_id": traffic_source_lead_id,
        "aged_data": aged_data,
        "jornaya_leadid": jornaya_leadid,
        "trusted_form_cert_url": trusted_form_cert_url,
        "tcpa_opt_in": tcpa_opt_in,
        "tcpa_optin_consent_language": tcpa_optin_consent_language,
        "payment_method_available": payment_method_available,
        "monthly_affordable_payment_amount": monthly_affordable_payment_amount,
        "jornaya_lead_id_agent": jornaya_lead_id_agent,
        "trusted_form_cert_url_agent": trusted_form_cert_url_agent,
        "traffic_source_data_list_id": traffic_source_data_list_id,
        "traffic_source_agent_id": traffic_source_agent_id,
        "traffic_source_agent_name": traffic_source_agent_name,
        "traffic_source_agent_recording_url": traffic_source_agent_recording_url,
        "ea_disposition": ea_disposition,
        "media_type": media_type,
    }

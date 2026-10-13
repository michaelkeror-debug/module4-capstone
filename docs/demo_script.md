(venv) MAC@MacBook-Air module4-capstone % curl localhost:8080/health
{"service":"triage-api","version":"1.0.0","status":"healthy"}%                                       
(venv) MAC@MacBook-Air module4-capstone % TOKEN=$(curl -s -X POST localhost:8080/token -H "Content-Type: application/json" -d '{"username":"mercy","password":"logistics2026"}' | python -c "import sys,json;print(json.load(sys.stdin)['access_token'])")
(venv) MAC@MacBook-Air module4-capstone % 
curl -X POST localhost:8080/triage -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"patient_message":"child has fever","county":"Nairobi"}'
{"urgency":"low","advice":"Rest, drink fluids, and monitor your symptoms. Seek medical care if symptoms worsen.","model_used":"triage-stub-v1","handled_for":"mercy"}%                                    
(venv) MAC@MacBook-Air module4-capstone % 

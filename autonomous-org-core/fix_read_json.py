with open('autonomous-org-core/agents/server.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace("data = self.read_json_body()", "# parsed above")
with open('autonomous-org-core/agents/server.py', 'w', encoding='utf-8') as f:
    f.write(code)
print("Cleaned self.read_json_body calls in server.py")

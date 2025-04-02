import json

# Generowanie listy hostów z podanych podsieci
hosts = [f"10.10.24.{i}" for i in range(1, 255)] + [f"10.10.25.{i}" for i in range(1, 255)]

# Struktura dynamicznego inwentarza Ansible
inventory = {
    "all": {
        "hosts": hosts,
        "vars": {
            "ansible_user": "your_user",
            "ansible_ssh_private_key_file": "~/.ssh/id_rsa"
        }
    }
}

# Wydrukowanie inwentarza w formacie JSON
print(json.dumps(inventory, indent=4))

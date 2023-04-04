#!/bin/bash

# Vérifier si le script a les permissions d'exécution
if ! [[ -x "$0" ]]; then
    echo "Le script n'a pas les permissions d'exécution."
    read -s -p "Veuillez saisir le mot de passe pour donner les permissions d'exécution au script : " password
    echo $password | sudo -S chmod +x "$0"
    echo "Permissions d'exécution accordées."
fi

# Créer un fichier de service pour le script Bash
echo "[Unit]
Description=Service Bash
After=network.target

[Service]
ExecStart=/bin/bash /path/to/your_repository/script_bash.sh

[Install]
WantedBy=multi-user.target" > service_bash.service

# Copier le fichier de service sur la machine cible
sudo cp service_bash.service /etc/systemd/system

# Activer le service Bash sur la machine cible
sudo systemctl enable service_bash.service
sudo systemctl start service_bash.service

# Exécuter le script Python sur la machine cible
python /path/to/your_repository/script_python.py

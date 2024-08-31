
# Zero-Trust Network Implementation

## Overview
This repository demonstrates the implementation of a Zero-Trust security model in a small to medium-sized network. The project includes configurations, scripts, and documentation for securing network communications, identity management, micro-segmentation, and continuous monitoring.

## Features
- **Identity Management**: OAuth2-based authentication and authorization using Flask and Authlib.
- **Network Segmentation**: Implemented using iptables to enforce micro-segmentation.
- **Encryption**: TLS configuration for secure communications via Nginx.
- **Continuous Monitoring**: Logstash configuration for monitoring and logging network activities.
- **Automation**: Ansible playbooks for automating the deployment of network configurations.

## Repository Structure
```plaintext
zero-trust-network/
├── architecture/
│   ├── diagrams/
# Script to generate architecture diagram
│   │   └── architecture.png            # Generated architecture diagram
│   └── design_document.md              # Design document
├── implementation/
│   ├── configuration_files/
│   │   ├── firewall_rules.sh           # Firewall rules for micro-segmentation
│   │   ├── nginx_tls.conf              # TLS configuration for Nginx
│   └── identity_management/
│       ├── oauth_config.py             # OAuth2 configuration using .env
│       └── .env.copy                   # Example environment variable file
├── automation/
│   ├── ansible/
│   │   └── playbook.yml                # Ansible playbook for automation
├── testing/
│   ├── test_cases/
│   │   └── test_identity_management.py # Unit tests for identity management
│   ├── penetration_testing/
│   │   └── pen_test_report.md          # Penetration testing report
│   └── validation_results.md           # Validation results
├── docs/
│   ├── user_guide.md                   # User guide
│   ├── developer_guide.md              # Developer guide
│   └── security_audit_report.md        # Security audit report
├── requirements.txt                    # Required Python packages
├── LICENSE                             # License file
└── README.md                           # Main README file with instructions
```

## Getting Started

### Prerequisites
- **Python 3.8+**
- **pip** (Python package installer)
- **nginx**
- **iptables**
- **Ansible**

### Setup Instructions

#### 1. Clone the Repository
```bash
git remote add origin https://github.com/Muhammad-H-Arif/Zero-Trust-Network.git
cd zero-trust-network
```

#### 2. Create a Virtual Environment
It's recommended to create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Required Python Packages
Install the necessary Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
Copy the `.env.copy` file to `.env` and fill in your specific values:

```bash
cp implementation/identity_management/.env.copy implementation/identity_management/.env
```

Edit the `.env` file with your specific OAuth2 credentials:

```plaintext
AUTH0_CLIENT_ID=your_auth0_client_id
AUTH0_CLIENT_SECRET=your_auth0_client_secret
AUTH0_DOMAIN=your_auth0_domain
```

#### 5. Run the Identity Management Service
Navigate to the `identity_management` directory and run the Flask app:

```bash
cd implementation/identity_management
python oauth_config.py
```

This will start the OAuth2-based authentication service.

#### 6. Configure Network Segmentation
Run the provided shell script to set up iptables rules for network segmentation:

```bash
sudo bash implementation/configuration_files/firewall_rules.sh
```

#### 7. Configure Nginx for TLS
Deploy the Nginx TLS configuration:

```bash
sudo cp implementation/configuration_files/nginx_tls.conf /etc/nginx/sites-available/default
sudo systemctl restart nginx
```

Make sure your SSL certificates are placed in `/etc/nginx/ssl/` as specified in the configuration file.

#### 8. Automate Deployment with Ansible
Use the provided Ansible playbook to automate the deployment of network configurations:

```bash
ansible-playbook automation/ansible/playbook.yml -i your_inventory_file
```

Replace `your_inventory_file` with your actual Ansible inventory file.

### Generating the Architecture Diagram

To generate the architecture diagram, navigate to the `architecture/diagrams/` directory and run the following command:

```bash
python generate_diagram.py
```

The diagram will be saved as `architecture.png`.

## Testing

### Unit Tests
Run the unit tests for the identity management system:

```bash
cd testing/test_cases
python -m unittest test_identity_management.py
```

### Penetration Testing
Refer to the `penetration_testing/pen_test_report.md` for details on the penetration testing conducted on this implementation.

## Documentation

- **User Guide**: Detailed instructions on using and maintaining the Zero-Trust Network can be found in `docs/user_guide.md`.
- **Developer Guide**: For developers looking to extend or modify the implementation, refer to `docs/developer_guide.md`.
- **Security Audit Report**: A summary of the security audit is available in `docs/security_audit_report.md`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


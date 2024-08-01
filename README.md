Due to time constrain unable to spin up EC2 Instance



1. Create and Deploy a Web Server
We’ll use AWS EC2 to create a web server and Ansible as our configuration management tool.

Ansible Playbook:

---
- name: Setup web server
  hosts: webservers
  become: yes
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present

    - name: Start and enable Apache
      service:
        name: httpd
        state: started
        enabled: yes

    - name: Create index.html
      copy:
        content: |
          <html>
          <head>
          <title>Hello World</title>
          </head>
          <body>
          <h1>Hello World!</h1>
          </body>
          </html>
        dest: /var/www/html/index.html

2. Secure the Application
We’ll use AWS Security Groups to ensure only appropriate ports are exposed and Let’s Encrypt for HTTPS redirection.

Ansible Playbook for Security:

---
- name: Secure web server
  hosts: webservers
  become: yes
  tasks:
    - name: Install Certbot
      yum:
        name: certbot
        state: present

    - name: Obtain SSL certificate
      command: certbot certonly --standalone --agree-tos --email your-email@example.com -d your-domain.com

    - name: Configure Apache for HTTPS
      copy:
        content: |
          <VirtualHost *:80>
              ServerName your-domain.com
              Redirect permanent / https://your-domain.com/
          </VirtualHost>

          <VirtualHost *:443>
              ServerName your-domain.com
              DocumentRoot /var/www/html
              SSLEngine on
              SSLCertificateFile /etc/letsencrypt/live/your-domain.com/fullchain.pem
              SSLCertificateKeyFile /etc/letsencrypt/live/your-domain.com/privkey.pem
          </VirtualHost>
        dest: /etc/httpd/conf.d/ssl.conf

    - name: Restart Apache
      service:
        name: httpd
        state: restarted

3. Automated Tests
We’ll use Inspec to validate the server configuration.

Inspec Test:

Ruby

describe http('http://your-domain.com', enable_remote_worker: true) do
  its('status') { should cmp 301 }
  its('headers.Location') { should cmp 'https://your-domain.com/' }
end

describe http('https://your-domain.com', ssl_verify: false) do
  its('status') { should cmp 200 }
  its('body') { should match /Hello World!/ }
end

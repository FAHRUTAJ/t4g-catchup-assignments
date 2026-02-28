# Web Architecture Reflection

## 1. What happens when I type a URL and press Enter?

When I type a URL into my browser:

1. **DNS Lookup**  
   The browser contacts a DNS server to translate the domain name (e.g., example.com) into an IP address.

2. **Firewall Check**  
   The request passes through firewalls that check whether the traffic is allowed or blocked.

3. **Load Balancer**  
   The request reaches a load balancer, which distributes traffic across multiple servers to prevent overload.

4. **Web Server**  
   The web server (like Nginx or Apache) receives the request and serves static files or forwards dynamic requests.

5. **Application Server**  
   The application server processes logic (e.g., login validation).

6. **Database**  
   The app server queries the database for needed data and sends the result back through the web server to the browser.

---

## 2. Difference Between Web Server and Application Server

A web server handles static content like HTML, CSS, and images.

An application server handles business logic and dynamic processing.

Example:
If I run an online clothing store:
- The web server serves product images.
- The application server processes checkout and payment logic.

---

## 3. Why the Client Never Talks Directly to the Database

The client cannot directly access the database because:

- Security risks
- Data integrity issues
- Business logic must be enforced
- Authentication must be controlled

The database is protected behind the application server.
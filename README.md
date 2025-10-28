# System Design Learning Path for SDE 1 → SDE 2 Promotion

## 🎯 **7 Core Concepts to Master**

### **1. Load Balancing**
Distribute requests across multiple servers
- **Algorithms**: Round Robin, Least Connections, Weighted, IP Hash
- **Tools**: Nginx, HAProxy, AWS ALB

### **2. Caching Strategies**
Store frequently accessed data in fast storage
- **Types**: Redis, Memcached, CDN, Application Cache
- **Patterns**: Write-through, Write-behind, Cache-aside

### **3. Database Connection Pooling**
Reuse database connections for better performance
- **Benefits**: Faster response, resource efficiency
- **Tools**: pgBouncer, HikariCP, connection pooling

### **4. Rate Limiting**
Control request frequency to prevent abuse
- **Strategies**: Token Bucket, Sliding Window, Fixed Window
- **Tools**: Redis, AWS API Gateway, Nginx

### **5. Database Indexing**
Speed up database queries with data structures
- **Types**: Primary, Secondary, Composite, Partial
- **Optimization**: Query analysis, index selection

### **6. Microservices Communication**
Services talking to each other in distributed systems
- **Patterns**: HTTP/REST, gRPC, Message Queues
- **Tools**: Service Mesh, API Gateway, Circuit Breakers

### **7. Message Queues**
Asynchronous communication between services
- **Use Cases**: Background processing, Event-driven architecture
- **Tools**: Kafka, RabbitMQ, AWS SQS

## 🚀 **Learning Path**

### **Week 1: Fundamentals**
- Load Balancing + Caching
- Database Connection Pooling + Indexing
- Rate Limiting

### **Week 2: Advanced**
- Microservices Communication
- Message Queues
- Integration and Practice

## 🎯 **Success Metrics**
- Design systems for 1M+ users
- Make informed technology decisions
- Communicate design decisions clearly
- Ready for SDE 2 promotion

---

**Focus on understanding the "why" behind each design decision.**
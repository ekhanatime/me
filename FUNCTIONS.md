# Functional Requirements

## User Management
```mermaid
flowchart TD
  A[Register] --> B[Get Me#ID]
  B --> C[Build Profile]
  C --> D[Skill Verification]
```

### Registration Flow
1. Frontend collects email/password
2. POST to `/api/register`
3. Server hashes password
4. Stores user in database

## Help Interactions
1. **Request Help**
   - Tag skills needed
   - Set urgency level
2. **Provide Help**
   - Solution submission
   - Rating received
   - Chain inheritance

## Session Handling
- **First Visit:** Assign temporary Me#ID stored in session cookie
- **Authentication:** 
  - Email/password or OAuth login
  - Merge temporary ID with permanent account
- **Returning Users:** Restore session from cookie

## Authentication
- Secure user registration
- Password hashing
- Session management
- OAuth integration (future)

## Game Systems
```mermaid
flowchart LR
  A[Help Given] --> B[XP]
  B --> C[Level Up]
  C --> D[Unlock Cosmetics]
  D --> E[Social Prestige]
```

## Database Requirements
- SQLite-compatible schema design
- JSON1 extension for skill storage
- Migration-ready structure

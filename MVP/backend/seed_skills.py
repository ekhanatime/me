from mvp_server import app, db, PersonalSkill, ProfessionalSkill

with app.app_context():
    db.create_all()
    
    personal_skills = ['Creative Thinking', 'Adaptability', 'Time Management']
    professional_skills = ['Project Management', 'Team Leadership', 'Technical Writing']
    
    for skill in personal_skills:
        db.session.add(PersonalSkill(name=skill))
    
    for skill in professional_skills:
        db.session.add(ProfessionalSkill(name=skill))
    
    db.session.commit()
    print('Database seeded successfully!')

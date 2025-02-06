import React, { useState } from 'react';
import SkillSelector from './SkillSelector';

export default function ProfileCard({ meId }) {
  const [skills, setSkills] = useState([]);
  
  return (
    <div className="profile-card">
      <h1>{meId}</h1>
      <SkillSelector 
        category="Personal Skills"
        skills={['Teaching', 'Listening', 'Empathy']}
        selected={skills}
        setSelected={setSkills}
      />
      <button className="help-button">Let's Help Someone</button>
    </div>
  );
}

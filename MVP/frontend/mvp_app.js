// Fetch user data
fetch('http://localhost:5000/api/user')
  .then(response => response.json())
  .then(data => {
    document.getElementById('me-id').textContent = data.me_id;
  })
  .catch(error => console.error('Error:', error));

// Fetch personal skills
fetch('http://localhost:5000/api/skills/personal')
  .then(response => response.json())
  .then(skills => renderSkills(skills, 'personal'))
  .catch(error => console.error('Personal skills error:', error));

// Fetch professional skills
fetch('http://localhost:5000/api/skills/professional')
  .then(response => response.json())
  .then(skills => renderSkills(skills, 'professional'))
  .catch(error => console.error('Professional skills error:', error));

function renderSkills(skills, type) {
  const container = document.getElementById('skills');
  const heading = document.createElement('h4');
  heading.textContent = type.charAt(0).toUpperCase() + type.slice(1) + ' Skills';
  container.appendChild(heading);
  
  skills.forEach(skill => {
    const skillElem = document.createElement('div');
    skillElem.className = 'skill';
    skillElem.textContent = skill;
    container.appendChild(skillElem);
  });
}

function startHelping() {
  // TODO: Implement help flow
  alert('Redirecting to help interface...');
}

async function handleLogin() {
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;
  
  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    
    if (response.ok) {
      window.location.href = '/profile';
    } else {
      alert('Invalid credentials');
    }
  } catch (error) {
    alert('Login failed');
  }
}

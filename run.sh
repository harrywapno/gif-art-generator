# Install Python dependencies
pip install -r backend/requirements.txt --user

# Install Node.js dependencies
cd frontend
npm install

# Start the Flask app in the background
cd ../backend
python app.py &

# Start the Node.js server in the background
cd ../frontend
npm start &

# Generate GIFs
curl -X POST -H "Content-Type: application/json" -d '{"parameters": [0.1, 0.2, 0.3, 0.4, 0.5]}' http://localhost:3000/generate_gif
curl -X POST -H "Content-Type: application/json" -d '{"parameters": [0.5, 0.4, 0.3, 0.2, 0.1]}' http://localhost:3000/generate_gif

# Get GIFs
curl http://localhost:3000/get_gif?gif_id=1
curl http://localhost:3000/get_gif?gif_id=2

from flask import Flask, jsonify, request
from models.model import GAN
from utils.data_loader import DataLoader
from utils.image_utils import save_image
from config.config import Config
from database.database import Database

app = Flask(__name__)
app.config.from_object(Config)

database = Database()

gan = GAN()
gan.load_models()

data_loader = DataLoader()

@app.route('/generate_gif', methods=['POST'])
def generate_gif():
    data = request.get_json()
    parameters = data['parameters']
    image = gan.generate_image(parameters)
    gif_id = database.save_gif(parameters, image)
    save_image(image, f'{gif_id}.gif')
    return jsonify({'gif_id': gif_id})

@app.route('/get_gif', methods=['GET'])
def get_gif():
    gif_id = request.args.get('gif_id')
    gif = database.get_gif(gif_id)
    return jsonify({'gif': gif})

if __name__ == '__main__':
    app.run()

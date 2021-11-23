from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.post("/")
async def root(request: Request) -> dict:
    """[summary]

    Args:
        request (Request): [description]

    Returns:
        [type]: [description]
    """    
    data = await request.json()
    if data.get('room') == 'activity-room':
        alerts = []
        if data['values'].get('co2') >= 500:
            alerts.append('co2')
        if (data['values'].get('temperature') <= 19) | (data['values'].get('temperature') >= 22):
            alerts.append('temperature')
        if (data['values'].get('humidity') <= 50) | (data['values'].get('humidity') >= 60):
            alerts.append('humidity')
        if (data['values'].get('sound') <= 0) | (data['values'].get('sound') >= 40):
            alerts.append('sound')
        if (data['values'].get('illumination') <= 300) | (data['values'].get('illumination') >= 750):
            alerts.append('illumination')

    elif data.get('room') == 'refectory':
        alerts = []
        if data['values'].get('co2') >= 400:
            alerts.append('co2')
        if (data['values'].get('temperature') <= 20) | (data['values'].get('temperature') >= 23):
            alerts.append('temperature')
        if (data['values'].get('humidity') <= 50) | (data['values'].get('humidity') >= 70):
            alerts.append('humidity')
        if (data['values'].get('sound') <= 20) | (data['values'].get('sound') >= 30):
            alerts.append('sound')
        if (data['values'].get('illumination') <= 200) | (data['values'].get('illumination') >= 500):
            alerts.append('illumination')

    elif data.get('room') == 'room-1':
        alerts = []
        if data['values'].get('co2') >= 300:
            alerts.append('co2')
        if (data['values'].get('temperature') <= 21) | (data['values'].get('temperature') >= 23):
            alerts.append('temperature')
        if (data['values'].get('humidity') <= 50) | (data['values'].get('humidity') >= 60):
            alerts.append('humidity')
        if (data['values'].get('sound') <= 10) | (data['values'].get('sound') >= 30):
            alerts.append('sound')
        if (data['values'].get('illumination') <= 100) | (data['values'].get('illumination') >= 200):
            alerts.append('illumination')

    elif data.get('room') == 'bathroom-main':
        alerts = []
        if data['values'].get('co2') >= 500:
            alerts.append('co2')
        if (data['values'].get('temperature') <= 22) | (data['values'].get('temperature') >= 25):
            alerts.append('temperature')
        if (data['values'].get('humidity') <= 60) | (data['values'].get('humidity') >= 75):
            alerts.append('humidity')
        if (data['values'].get('sound') <= 20) | (data['values'].get('sound') >= 35):
            alerts.append('sound')
        if (data['values'].get('illumination') <= 100) | (data['values'].get('illumination') >= 200):
            alerts.append('illumination')

    elif data.get('room') == 'garden':
        alerts = []
        if data['values'].get('co2') >= 500:
            alerts.append('co2')
        if (data['values'].get('temperature') <= 15) | (data['values'].get('temperature') >= 22):
            alerts.append('temperature')
        if (data['values'].get('humidity') <= 50) | (data['values'].get('humidity') >= 80):
            alerts.append('humidity')
        if (data['values'].get('sound') <= 10) | (data['values'].get('sound') >= 35):
            alerts.append('sound')
    return {"alerts": alerts}

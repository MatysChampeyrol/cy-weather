// Types pour les données météo

export interface CurrentWeatherData {
    temperature: number;
    feels_like: number;
    humidity: number;
    pressure: number;
    wind_speed: number;
    description: string;
    icon: string;
}

export interface WeatherResponse {
    city: string;
    country: string;
    timestamp: string;
    weather: CurrentWeatherData;
}

export interface DailyForecastData {
    date: string;
    temp_min: number;
    temp_max: number;
    temp_day: number;
    temp_night: number;
    humidity: number;
    wind_speed: number;
    description: string;
    icon: string;
    precipitation_probability: number | null;
}

export interface ForecastResponse {
    city: string;
    country: string;
    forecast: DailyForecastData[];
}

<script setup lang="ts">
import type { WeatherResponse } from '../types/weather';

interface Props {
  weather: WeatherResponse | null;
  loading: boolean;
  error: string | null;
}

defineProps<Props>();

const getWeatherIcon = (icon: string) => {
  return `https://openweathermap.org/img/wn/${icon}@2x.png`;
};

const formatDate = (timestamp: string) => {
  return new Date(timestamp).toLocaleString('fr-FR', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
};
</script>

<template>
  <div class="current-weather">
    <h2>Météo actuelle</h2>
    
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Chargement...</p>
    </div>

    <div v-else-if="error" class="error">
      <p>❌ {{ error }}</p>
    </div>

    <div v-else-if="weather" class="weather-content">
      <div class="location">
        <h3>{{ weather.city }}, {{ weather.country }}</h3>
        <p class="timestamp">{{ formatDate(weather.timestamp) }}</p>
      </div>

      <div class="weather-main">
        <div class="icon-temp">
          <img :src="getWeatherIcon(weather.weather.icon)" :alt="weather.weather.description" />
          <div class="temperature">
            <span class="temp-value">{{ Math.round(weather.weather.temperature) }}°</span>
            <span class="temp-unit">C</span>
          </div>
        </div>
        <p class="description">{{ weather.weather.description }}</p>
      </div>

      <div class="weather-details">
        <div class="detail-item">
          <span class="detail-label">Ressenti</span>
          <span class="detail-value">{{ Math.round(weather.weather.feels_like) }}°C</span>
        </div>
        <div class="detail-item">
          <span class="detail-label">Humidité</span>
          <span class="detail-value">{{ weather.weather.humidity }}%</span>
        </div>
        <div class="detail-item">
          <span class="detail-label">Pression</span>
          <span class="detail-value">{{ weather.weather.pressure }} hPa</span>
        </div>
        <div class="detail-item">
          <span class="detail-label">Vent</span>
          <span class="detail-value">{{ weather.weather.wind_speed }} m/s</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.current-weather {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  padding: 2rem;
  color: white;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

h2 {
  margin: 0 0 1.5rem 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
}

.spinner {
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid white;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error {
  background: rgba(255, 0, 0, 0.2);
  border-radius: 10px;
  padding: 1rem;
}

.weather-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.location h3 {
  margin: 0;
  font-size: 1.8rem;
  font-weight: 700;
}

.timestamp {
  margin: 0.5rem 0 0 0;
  opacity: 0.9;
  font-size: 0.9rem;
}

.weather-main {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.icon-temp {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.icon-temp img {
  width: 100px;
  height: 100px;
  filter: drop-shadow(0 2px 10px rgba(0, 0, 0, 0.2));
}

.temperature {
  display: flex;
  align-items: flex-start;
}

.temp-value {
  font-size: 4rem;
  font-weight: 700;
  line-height: 1;
}

.temp-unit {
  font-size: 2rem;
  font-weight: 300;
  margin-top: 0.5rem;
}

.description {
  font-size: 1.2rem;
  text-transform: capitalize;
  margin: 0;
  opacity: 0.95;
}

.weather-details {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}

.detail-item {
  background: rgba(255, 255, 255, 0.15);
  padding: 1rem;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  backdrop-filter: blur(10px);
}

.detail-label {
  font-size: 0.85rem;
  opacity: 0.9;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.detail-value {
  font-size: 1.3rem;
  font-weight: 600;
}

@media (min-width: 768px) {
  .weather-details {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>

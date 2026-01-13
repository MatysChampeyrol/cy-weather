<script setup lang="ts">
import type { ForecastResponse } from '../types/weather';

interface Props {
  forecast: ForecastResponse | null;
  loading: boolean;
  error: string | null;
}

defineProps<Props>();

const getWeatherIcon = (icon: string) => {
  return `https://openweathermap.org/img/wn/${icon}@2x.png`;
};

const formatDate = (dateStr: string) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('fr-FR', {
    weekday: 'short',
    day: 'numeric',
    month: 'short',
  });
};

const getDayName = (dateStr: string) => {
  const date = new Date(dateStr);
  const today = new Date();
  const tomorrow = new Date(today);
  tomorrow.setDate(tomorrow.getDate() + 1);

  if (date.toDateString() === today.toDateString()) {
    return "Aujourd'hui";
  } else if (date.toDateString() === tomorrow.toDateString()) {
    return "Demain";
  }
  return date.toLocaleDateString('fr-FR', { weekday: 'long' });
};
</script>

<template>
  <div class="forecast">
    <h2>Prévisions sur 7 jours</h2>
    
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Chargement des prévisions...</p>
    </div>

    <div v-else-if="error" class="error">
      <p>❌ {{ error }}</p>
    </div>

    <div v-else-if="forecast" class="forecast-content">
      <div class="forecast-location">
        <h3>{{ forecast.city }}, {{ forecast.country }}</h3>
      </div>

      <div class="forecast-grid">
        <div 
          v-for="(day, index) in forecast.forecast" 
          :key="index" 
          class="forecast-card"
          :class="{ 'today': index === 0 }"
        >
          <div class="day-header">
            <h4>{{ getDayName(day.date) }}</h4>
            <p class="date">{{ formatDate(day.date) }}</p>
          </div>

          <img 
            :src="getWeatherIcon(day.icon)" 
            :alt="day.description"
            class="weather-icon"
          />

          <p class="description">{{ day.description }}</p>

          <div class="temperatures">
            <div class="temp-range">
              <span class="temp-max">{{ Math.round(day.temp_max) }}°</span>
              <span class="temp-separator">/</span>
              <span class="temp-min">{{ Math.round(day.temp_min) }}°</span>
            </div>
          </div>

          <div class="day-details">
            <div class="detail" v-if="day.precipitation_probability !== null">
              <span class="icon">💧</span>
              <span>{{ Math.round(day.precipitation_probability) }}%</span>
            </div>
            <div class="detail">
              <span class="icon">💨</span>
              <span>{{ day.wind_speed.toFixed(1) }} m/s</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.forecast {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

h2 {
  margin: 0 0 1.5rem 0;
  font-size: 1.5rem;
  font-weight: 600;
  color: #333;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #667eea;
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
  background: #fee;
  border-radius: 10px;
  padding: 1rem;
  color: #c00;
}

.forecast-location h3 {
  margin: 0 0 1.5rem 0;
  font-size: 1.3rem;
  color: #555;
  font-weight: 600;
}

.forecast-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.forecast-card {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 15px;
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
  transition: transform 0.2s, box-shadow 0.2s;
  position: relative;
}

.forecast-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.forecast-card.today {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.forecast-card.today .day-header h4,
.forecast-card.today .day-header .date,
.forecast-card.today .description,
.forecast-card.today .temperatures,
.forecast-card.today .day-details {
  color: white;
}

.day-header {
  text-align: center;
}

.day-header h4 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
  text-transform: capitalize;
}

.date {
  margin: 0.3rem 0 0 0;
  font-size: 0.85rem;
  color: #666;
  text-transform: capitalize;
}

.weather-icon {
  width: 80px;
  height: 80px;
  filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.1));
}

.description {
  font-size: 0.9rem;
  text-align: center;
  margin: 0;
  color: #555;
  text-transform: capitalize;
  min-height: 2.5em;
}

.temperatures {
  width: 100%;
}

.temp-range {
  display: flex;
  justify-content: center;
  align-items: baseline;
  gap: 0.5rem;
  font-size: 1.3rem;
  font-weight: 600;
}

.temp-max {
  color: #e74c3c;
}

.temp-min {
  color: #3498db;
}

.forecast-card.today .temp-max,
.forecast-card.today .temp-min {
  color: white;
}

.temp-separator {
  color: #999;
  font-weight: 400;
}

.day-details {
  display: flex;
  gap: 1rem;
  justify-content: center;
  width: 100%;
  padding-top: 0.5rem;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.forecast-card.today .day-details {
  border-top-color: rgba(255, 255, 255, 0.3);
}

.detail {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.85rem;
  color: #666;
}

.detail .icon {
  font-size: 1rem;
}

@media (max-width: 768px) {
  .forecast-grid {
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  }
  
  .forecast-card {
    padding: 1rem 0.5rem;
  }
  
  .weather-icon {
    width: 60px;
    height: 60px;
  }
}
</style>

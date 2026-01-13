<script setup lang="ts">
import { ref } from 'vue';
import CurrentWeather from './components/CurrentWeather.vue';
import WeatherForecast from './components/WeatherForecast.vue';
import { getCurrentWeather, getWeatherForecast } from './api/api';
import type { WeatherResponse, ForecastResponse } from './types/weather';

const city = ref('Paris');
const countryCode = ref('FR');
const currentWeather = ref<WeatherResponse | null>(null);
const forecast = ref<ForecastResponse | null>(null);
const loadingCurrent = ref(false);
const loadingForecast = ref(false);
const errorCurrent = ref<string | null>(null);
const errorForecast = ref<string | null>(null);

async function fetchWeather() {
  if (!city.value.trim()) {
    errorCurrent.value = 'Veuillez entrer un nom de ville';
    errorForecast.value = 'Veuillez entrer un nom de ville';
    return;
  }

  // Fetch météo actuelle
  loadingCurrent.value = true;
  errorCurrent.value = null;
  try {
    currentWeather.value = await getCurrentWeather(
      city.value,
      countryCode.value || undefined
    );
  } catch (error) {
    errorCurrent.value = error instanceof Error ? error.message : 'Erreur lors de la récupération des données';
    currentWeather.value = null;
  } finally {
    loadingCurrent.value = false;
  }

  // Fetch prévisions
  loadingForecast.value = true;
  errorForecast.value = null;
  try {
    forecast.value = await getWeatherForecast(
      city.value,
      countryCode.value || undefined
    );
  } catch (error) {
    errorForecast.value = error instanceof Error ? error.message : 'Erreur lors de la récupération des prévisions';
    forecast.value = null;
  } finally {
    loadingForecast.value = false;
  }
}

// Charger la météo au montage du composant
fetchWeather();
</script>

<template>
  <div class="app">
    <header class="header">
      <h1>🌤️ CY Weather</h1>
      <p class="subtitle">Votre météo en temps réel</p>
    </header>

    <div class="search-section">
      <div class="search-form">
        <div class="input-group">
          <input
            v-model="city"
            @keyup.enter="fetchWeather"
            type="text"
            placeholder="Nom de la ville"
            class="city-input"
          />
          <input
            v-model="countryCode"
            @keyup.enter="fetchWeather"
            type="text"
            placeholder="Code pays (ex: FR)"
            class="country-input"
            maxlength="2"
          />
        </div>
        <button @click="fetchWeather" class="search-button">
          🔍 Rechercher
        </button>
      </div>
    </div>

    <main class="content">
      <CurrentWeather 
        :weather="currentWeather"
        :loading="loadingCurrent"
        :error="errorCurrent"
      />

      <WeatherForecast 
        :forecast="forecast"
        :loading="loadingForecast"
        :error="errorForecast"
      />
    </main>

    <footer class="footer">
      <p>Données fournies par <a href="https://open-meteo.com/" target="_blank">Open-Meteo</a></p>
    </footer>
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  background: linear-gradient(to bottom, #e0f7ff 0%, #fff 100%);
  padding: 2rem;
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.header h1 {
  font-size: 3rem;
  margin: 0;
  color: #2c3e50;
  font-weight: 700;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  margin: 0.5rem 0 0 0;
}

.search-section {
  max-width: 600px;
  margin: 0 auto 3rem;
}

.search-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.input-group {
  display: flex;
  gap: 0.5rem;
}

.city-input,
.country-input {
  padding: 1rem;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.city-input {
  flex: 2;
}

.country-input {
  flex: 1;
  text-transform: uppercase;
}

.city-input:focus,
.country-input:focus {
  outline: none;
  border-color: #667eea;
}

.search-button {
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.search-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.search-button:active {
  transform: translateY(0);
}

.content {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.footer {
  text-align: center;
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid #e0e0e0;
  color: #7f8c8d;
}

.footer a {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
}

.footer a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .app {
    padding: 1rem;
  }

  .header h1 {
    font-size: 2rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .input-group {
    flex-direction: column;
  }

  .city-input,
  .country-input {
    width: 100%;
  }
}
</style>


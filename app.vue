<template>
  <div class="prediction-form">
    <div class="input-group">
      <label for="age">Age:</label>
      <input id="age" v-model.number="age" placeholder="Enter age" type="number">
    </div>
    <div class="input-group">
      <label for="salary">Salary ($):</label>
      <input id="salary" v-model.number="salary" placeholder="Enter salary" type="number">
    </div>
    <button @click="makePrediction">Predict Purchase</button>
    <p v-if="prediction !== null" class="prediction-result">
      {{ predictionMessage }}
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  setup() {
    const age = ref(null);
    const salary = ref(null);
    const prediction = ref(null);

    const makePrediction = async () => {
      try {
        const response = await axios.post('http://localhost:3000/predict', {
          age: age.value,
          salary: salary.value
        });
        prediction.value = response.data.prediction;
      } catch (error) {
        console.error(error);
      }
    };

    const predictionMessage = computed(() => {
      return prediction.value === 1
        ? `Based on the data, this person is likely to purchase.`
        : `Based on the data, this person is unlikely to purchase.`;
    });

    return {
      age,
      salary,
      prediction,
      makePrediction,
      predictionMessage
    }
  }
}
</script>

<style lang="scss">
.prediction-form {
  max-width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

  .input-group {
    margin-bottom: 10px;

    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }

    input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
      box-sizing: border-box;
    }
  }

  button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;

    &:hover {
      background-color: #4cae4c;
    }
  }

  .prediction-result {
    margin-top: 20px;
    padding: 10px;
    background-color: #f2f2f2;
    border: 1px solid #ddd;
    border-radius: 4px;
    text-align: center;
  }
}
</style>

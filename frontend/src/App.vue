<template>
  <div class="container">
    <div class="left-side">
      <form @submit.prevent="submitForm">
        <div>
          <label for="loan">Loan:</label>
          <input type="number" id="loan" v-model="loan" required>
        </div>
        <div>
          <label for="installments_number">Installments Number:</label>
          <input type="number" id="installments_number" v-model="installments_number" required>
        </div>
        <div>
          <label for="interest">Interest:</label>
          <input type="number" step="0.01" id="interest" v-model="interest" required>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
    <div class="right-side">
      <canvas id="amortizationChart"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
  data() {
    return {
      loan: null,
      installments_number: null,
      interest: null,
      chart: null
    };
  },
  methods: {
    submitForm() {
      axios.post('http://localhost:8000/api/sac/', {
        loan: this.loan,
        installments_number: this.installments_number,
        interest: this.interest
      }).then((response) => {
        // console.log(response);
        this.updateChart(response.data);
      }).catch((error) => {
        console.log(error);
      });
    },
    updateChart(response) {
      if (!this.chart) {
        console.log(response);
        const ctx = document.getElementById('amortizationChart').getContext('2d');
        this.chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: response.map(item => item.installments_number),
            datasets: [{
              label: 'Balance Due',
              data: response.map(item => item.balance_due),
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1,
            }]
          },
          options: {
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Month'
                }
              }
            }
          }
        });
      }
      // this.chart.update();
    }

  }
};
</script>
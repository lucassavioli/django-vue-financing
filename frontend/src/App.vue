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
    <div v-if="data">
      <div>
        <h1>Sac Table</h1>
        <table>
          <thead>
            <tr>
              <th>Installments Number</th>
              <th>Installment</th>
              <th>Interest</th>
              <th>Amortization</th>
              <th>Balance Due</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in data.sac" :key="item.installments_number">
              <td>{{ item.installments_number }}</td>
              <td>{{ item.installment }}</td>
              <td>{{ item.interest }}</td>
              <td>{{ item.amortization }}</td>
              <td>{{ item.balance_due }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div>
        <h1>Price Table</h1>
        <table>
          <thead>
            <tr>
              <th>Installments Number</th>
              <th>Installment</th>
              <th>Interest</th>
              <th>Amortization</th>
              <th>Balance Due</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in data.price" :key="item.installments_number">
              <td>{{ item.installments_number }}</td>
              <td>{{ item.installment }}</td>
              <td>{{ item.interest }}</td>
              <td>{{ item.amortization }}</td>
              <td>{{ item.balance_due }}</td>
            </tr>
          </tbody>
        </table>
      </div>
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
      data: null,
      chart: null
    };
  },
  methods: {
    submitForm() {
      axios.post('http://localhost:8000/api/sacprice/', {
        loan: this.loan,
        installments_number: this.installments_number,
        interest: this.interest
      }).then((response) => {
        this.data = response.data;
        this.displayChart(this.data);
      }).catch((error) => {
        console.log(error);
      });
    },
    displayChart(data) {
      if (!this.chart) {
        console.log(data);
        const ctx = document.getElementById('amortizationChart').getContext('2d');
        this.chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: data.sac.map(item => item.installments_number),
            datasets: [{
              label: 'SAC',
              data: data.sac.map(item => item.amortization),
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1,
            },
            {
              label: 'PRICE',
              data: data.price.map(item => item.amortization),
              borderColor: 'rgb(75, 192, 55)',
              tension: 0.1,
            }
            ]
          },
          options: {
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Month'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'Amortization'
                }
              }
            }
          }
        });
      }
    }

  }
};
</script>
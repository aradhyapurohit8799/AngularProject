import { Component, OnInit } from '@angular/core';
import { EChartsOption } from 'echarts';
import { AnalyticsService } from 'src/app/features/dashboard/dashboard.service';

@Component({
  selector: 'app-area-chart-animated',
  templateUrl: './area-chart-animated.component.html',
  styleUrls: ['./area-chart-animated.component.scss'],
})
export class AreaChartAnimatedComponent implements OnInit {
  _chartOption: EChartsOption = {};

  constructor(private dashboard:AnalyticsService) {}

  ngOnInit() {
    this.dashboard.getbmihistogram().subscribe(data => {
      this.loadChart(data);
    })
    // this.loadChart();
  }

  private loadChart(data:any): void {
    const xAxisData = [];
    const data1 = data["bmiCharge"];
    // const data2 = [];

    // for (let i = 0; i < 100; i++) {
    //   xAxisData.push('category' + i);
    //   data1.push((Math.sin(i / 5) * (i / 5 - 10) + i / 6) * 5);
    //   data2.push((Math.cos(i / 5) * (i / 5 - 10) + i / 6) * 5);
    // }

    this._chartOption = {
      legend: {
        // data: ['bar', 'bar2'],
        data: ['BMI vs Charge'],
        align: 'left',
      },
      tooltip: {},
      xAxis: {
        // data: xAxisData,
        silent: false,
        splitLine: {
          show: false,
        },
        name: 'BMI',
        nameLocation: 'middle',
        nameGap: 50
      },
      yAxis: {
      name: 'Charge',
      nameLocation: 'middle',
      nameGap: 50},
      series: [
        { symbolSize: 5,
          name: 'BMI vs Charge',
          type: 'scatter',
          data: data1,
          animationDelay: (idx: number) => idx * 1,
        },
        // {
        //   name: 'bar2',
        //   type: 'bar',
        //   data: data2,
        //   animationDelay: (idx: number) => idx * 10 + 100,
        // },
      ],
      animationEasing: 'elasticOut',
      animationDelayUpdate: (idx: number) => idx * 1,
    };
  }
}

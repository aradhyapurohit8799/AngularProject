import { Component, Input, OnInit } from '@angular/core';
import { EChartsOption } from 'echarts';
import { AnalyticsService } from 'src/app/features/dashboard/dashboard.service';

@Component({
  selector: 'app-bar-chart',
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.scss'],
})
export class BarChartComponent implements OnInit {
  @Input() chartUrl = '';
  _chartOption: EChartsOption = {};
  private showLegend: boolean = true;

  constructor(private dashboard:AnalyticsService) {}

  ngOnInit() {
    // let data = [820, 932, 901, 934, 1290, 1330, 1320];
    // if (this.chartUrl === 'first') {
    //   data = [820, 932, 901, 934, 990, 930, 920];
    //   this.showLegend = false;
    // }
    // if (this.chartUrl === 'second') {
    //   data = [20, 32, 41, 34, 50, 30, 20];
    //   this.showLegend = false;
    // }
    // if (this.chartUrl === 'third') {
    //   data = [1820, 1932, 1901, 1934, 1990, 1930, 1920];
    //   this.showLegend = false;
    // }
    // console.log(this.chartUrl, this.showLegend);
    if (this.chartUrl==='first') {
      this.dashboard.getchildrencountplot().subscribe(data => {
        this.loadChart(data);
      })
    }
    if (this.chartUrl==='second') {
      this.dashboard.getagecountplot().subscribe(data => {
        this.loadChart(data);
      })
    }



    // this.loadChart(data);


  }

  private loadChart(data: any): void {
    let label:string = Object.keys(data)[0]
    let count:string = Object.keys(data)[1]
    console.log(data[label], data[count])
    this._chartOption = {
      xAxis: {
        type: 'category',
        boundaryGap: false,
        // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        data: data[label],
        show: this.showLegend,
        name: label,
        nameLocation: 'middle',
        nameGap: 50

      },
      yAxis: {
        type: 'value',
        show: this.showLegend,
        name: count,
        nameLocation: 'middle',
        nameGap: 50,

      },
      series: [
        {
          // data: [820, 932, 901, 934, 990, 930, 920],
          data: data[count],
          type: 'bar',
          animationDelay: (idx: number) => idx * 1,
          barWidth: '5%'

        },
      ],
    };
  }
}

import { HttpClient} from '@angular/common/http';
import { Component, OnInit, Input } from '@angular/core';
import { EChartsOption } from 'echarts';
import { AnalyticsService } from 'src/app/features/dashboard/dashboard.service';

@Component({
  selector: 'app-pie-chart',
  templateUrl: './pie-chart.component.html',
  styleUrls: ['./pie-chart.component.scss'],
})
export class PieChartComponent implements OnInit {
  @Input() chartUrl = '';
  _chartOption: EChartsOption = {};

  constructor( private http : HttpClient, private dashboard : AnalyticsService ) {}

  ngOnInit() {

    // this.InitPipe();
    if (this.chartUrl ==='first') {
      this.dashboard.getmvsfpichart().subscribe((data:any) => {
        this.InitPipe(data);
      })
    }
    if (this.chartUrl ==='second') {
      this.dashboard.getsmokerpiechart().subscribe((data:any) => {
        this.InitPipe(data);
      })
    }
    // let data = this.getDatasynchronously()
    // this.InitPipe(data.then(response => {return response}))
  }

//   getData() {
//     return this.http.get("http://127.0.0.1:5000/mvsfPieChart")
//  }
//   getDataSynchronous():Promise<any>{
//     console.log(this.getData().toPromise())
//    return this.getData().toPromise()
//  }
//  async getDatasynchronously() {
//   return await this.getDataSynchronous()
// }

  private InitPipe(data: any): void {
    // console.log(data)
    // var inx = 2;
    // if (this.chartUrl === 'first') {
    //   inx = 3;
    // }
    // if (this.chartUrl === 'second') {
    //   inx = 4;
    // }
    // if (this.chartUrl === 'third') {
    //   inx = 5;
    // }
    console.log(Object.keys(data)[0])
    let label:string = Object.keys(data)[0]
    let value:string = Object.keys(data)[1]
    console.log(typeof(label))
    let chartreq: any = [];
    for (let i = 0; i < data[label].length; i++) {
      chartreq.push({value:data[value][i], name:data[label][i]})
    }
    console.log(chartreq)

    this._chartOption = {
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)',
      },
      legend: {
        //selectedMode: false,
        orient: 'vertical',
        //x: 'left',
        // data: ['female', 'male'].slice(0, 2),
        data: data[label],
      },

      xAxis: {
        type: 'category',
        axisTick: {
          alignWithLabel: true,
        },
      },
      yAxis: {
        type: 'value',
      },
      series: [
        {
          name: 'Pie Chart',
          type: 'pie',
          radius: ['50%', '70%'],
          avoidLabelOverlap: false,
          // data: [
          //   { value: data["count"][0], name: data["sex"][0] },
          //   { value: data["count"][1], name: data["sex"][1]},
          // ].slice(0, data["sex"].length),
          data: chartreq,
        },
      ],

      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true,
      },
    };

    // console.log(data["count"][0])
  }
}

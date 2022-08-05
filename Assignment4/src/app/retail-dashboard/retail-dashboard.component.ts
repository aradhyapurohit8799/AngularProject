import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { AccessTokenService } from '../access-token.service';
import { averageSales } from '../averageSales';
import { totalSales } from '../totalSales';
import { uniqueCustomer } from '../uniqueCustomer';
import { dailySales } from '../DailySales'

@Component({
  selector: 'app-retail-dashboard',
  templateUrl: './retail-dashboard.component.html',
  styleUrls: ['./retail-dashboard.component.css']
})
export class RetailDashboardComponent implements OnInit {

  totalSales: number = 0;
  uniqueCustomer: number = 0;
  averageSales: number = 0;
  AccessToken: string = '';
  dailySales: any = [];


  constructor(private http: HttpClient, private _accessTokenService: AccessTokenService) { }

  ngOnInit(): void {

    this._accessTokenService.getAccessToken()
      .subscribe(data => {
        this.generateAccessToken(data.access_token);
      });
  }

  generateAccessToken(accessToken) {

    this.AccessToken = accessToken;
    if (this.AccessToken !== 'undefined') {
      this.http.get<totalSales>("http://127.0.0.1:5000/Total Sales Value").subscribe(data => {
        this.totalSales = data["Total Sales"];
      });

      this.http.get<averageSales>("http://127.0.0.1:5000/AVG").subscribe(data => {
        this.averageSales = data["Average Sales"];
      });
      this.http.get<uniqueCustomer>("http://127.0.0.1:5000/Unique").subscribe(data => {
        this.uniqueCustomer = data["unique cutomers"];
      });
      this.http.get<dailySales[]>("http://127.0.0.1:5000/total sales/1", { headers: new HttpHeaders({ "Authorization": "JWT " + accessToken }) }).subscribe(data => {
        this.dailySales = data["Items"];
      });
    } else {
      console.log(("Authentication not done"))
    }

  }

}

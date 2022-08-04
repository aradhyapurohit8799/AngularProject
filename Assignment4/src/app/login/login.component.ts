import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { accessToken } from '../accessToken'




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  accessToken: string = '';


  hide = true;

  constructor(private router: Router, private http: HttpClient) { }

  ngOnInit(): void {

  }


  OnLogin(username, password) {
    username = username;
    password = password;
    const headers = { 'Content-Type': 'application/json' };
    const body = { "username": username, "password": password };
    const _auth: string = "http://127.0.0.1:5000/auth";
    this.http.post<accessToken>(_auth, body, { headers }).subscribe(data => {
      this.accessToken = data.access_token;
    });

    if (username === "AP8799" && password === "asdf") {
      this.router.navigate(['/retail-dashboard']);
      this.hide = true;
    } else {
      this.hide = false
    }


  }

}

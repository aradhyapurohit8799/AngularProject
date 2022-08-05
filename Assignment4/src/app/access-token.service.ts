import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { accessToken } from './accessToken';


const headers = { 'Content-Type': 'application/json' };
const body = { "username": "AP8799", "password": "asdf" }
@Injectable({
  providedIn: 'root'
})
export class AccessTokenService {


  private _auth: string = "http://127.0.0.1:5000/auth";
  constructor(private http: HttpClient) { }

  getAccessToken(): Observable<accessToken> {
    return this.http.post<accessToken>(this._auth, body, { headers })
  };
}

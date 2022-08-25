import { Injectable, Inject, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { delay, map } from 'rxjs/operators';
import { catchError, Observable, switchMap, throwError } from 'rxjs';
import { addDays } from 'date-fns';
import { UserService } from '../../user/user.service';
import { environment } from '../../../../environments/environment';
import { of, EMPTY } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthenticationService {
  private _authenticated: boolean = false;
  constructor(
    private _httpClient: HttpClient,
    private _userService: UserService,
    @Inject('LOCALSTORAGE') private localStorage: Storage
  ) {}

  /**
   * Setter & getter for access token
   */
  // set accessToken(token: string) {
  //   localStorage.setItem('accessToken', token);
  // }

  // get accessToken(): string {
  //   return localStorage.getItem('accessToken') ?? '';
  // }

  accessToken : string = ''

  login(email: string, password: string) {
    return of(true).pipe(
      delay(1000),
      map((/*response*/) => {
        // set token property
        // const decodedToken = jwt_decode(response['token']);

        // store email and jwt token in local storage to keep user logged in between page refreshes
        this.localStorage.setItem(
          'currentUser',
          JSON.stringify({
            token: 'aisdnaksjdn,axmnczm',
            isAdmin: true,
            email: 'john.doe@gmail.com',
            id: '12312323232',
            alias: 'john.doe@gmail.com'.split('@')[0],
            expiration: addDays(Date.now(), 1), //moment().add(1, 'days').toDate(),
            fullName: 'John Doe',
          })
        );

        return true;
      })
    );
  }

  logout(): void {
    // clear token remove user from local storage to log user out
    this.localStorage.removeItem('currentUser');
  }

  getCurrentUser(): any {
    // TODO: Enable after implementation
    // return JSON.parse(this.localStorage.getItem('currentUser'));
    return {
      // token: 'aisdnaksjdn,axmnczm',
      // token: this.accessToken,
      token: window.sessionStorage.getItem("accessToken"),
      isAdmin: true,
      email: 'aradhya.purohit@tigeranalytics.com',
      id: '4112',
      alias: 'aradhya.purohit@tigeranalytics.com'.split('@')[0],
      expiration: addDays(Date.now(), 1), //moment().add(1, 'days').toDate(),
      fullName: 'Aradhya Purohit',
    };
  }

  passwordResetRequest(email: string) {
    return of(true).pipe(delay(1000));
  }

  changePassword(email: string, currentPwd: string, newPwd: string) {
    return of(true).pipe(delay(1000));
  }

  passwordReset(
    email: string,
    token: string,
    password: string,
    confirmPassword: string
  ): any {
    return of(true).pipe(delay(1000));
  }

  // signUp(user: {
  //   name: string;
  //   email: string;
  //   password: string;
  //   company: string;
  // }): Observable<any> {
  //   // return this._httpClient.post('api/auth/sign-up', user);
  //   return this._httpClient.post('http://127.0.0.1:5000/register', user);
  // }
  signUp(user: {
    id: string;
    firstname: string;
    lastname: string;
    username: string;
    password: string;
  }): Observable<any> {
    // return this._httpClient.post('api/auth/sign-up', user);
    return this._httpClient.post('http://127.0.0.1:5000/register', user);
  }

  /**
   * Sign out
   */
  signOut(): Observable<any> {
    // Remove the access token from the local storage
    localStorage.removeItem('accessToken');

    // Set the authenticated flag to false
    this._authenticated = false;

    // Return the observable
    return of(true);
  }

  /**
   * Sign in
   *
   * @param credentials
   */
  signIn(credentials: { username: string; password: string }): Observable<any> {
    // Throw error, if the user is already logged in
    if (this._authenticated) {

      return throwError('User is already logged in.');

    }

    return this._httpClient.post('http://127.0.0.1:5000/auth', credentials).pipe(
      switchMap((response: any) => {
        // Store the access token in the local storage
        // this.accessToken = response.accessToken;
        console.log("hello world")
        window.sessionStorage.setItem("accessToken", response.access_token)
        // this.accessToken = response.access_token;
        // this.accessToken = window.localStorage.getItem("accessToken");

        // Set the authenticated flag to true
        this._authenticated = true;
        console.log(response)
        console.log("Inside signIn function")

        // Store the user on the user service
        // this._userService.user = response.user;

        // Return a new observable with the response
        return of(response);
      })
    );

  }
}

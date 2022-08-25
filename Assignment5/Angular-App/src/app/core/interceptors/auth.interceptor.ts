import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpErrorResponse } from '@angular/common/http';
import { HttpRequest } from '@angular/common/http';
import { HttpHandler } from '@angular/common/http';
import { HttpEvent } from '@angular/common/http';
import { tap } from 'rxjs/operators';

import { AuthenticationService } from '../services/auth/auth.service';
import { MatDialog } from '@angular/material/dialog';

@Injectable({providedIn:"root"})
export class AuthInterceptor implements HttpInterceptor {
  constructor(
    private authService: AuthenticationService,
    private router: Router,
    private dialog: MatDialog
  ) {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    const user = this.authService.getCurrentUser();
    console.log(user.token)

    // if (user && user.token) {
    //   const cloned = req.clone({
    //     headers: req.headers.set('Authorization', 'Bearer ' + user.token),
    //   });
    if (user.token) {
      let access_token:string=user.token
      const cloned = req.clone({
        headers: req.headers.set('Authorization', 'JWT ' + access_token),
      });

      return next.handle(cloned).pipe(
        tap(
          () => {},
          (err: any) => {
            if (err instanceof HttpErrorResponse) {
              if (err.status === 401) {
                this.dialog.closeAll();
                this.router.navigate(['/auth/signin']);
                console.log("FAILED ACESS TOKEN")
              }
            }
          }
        )
      );
    } else {
      return next.handle(req);
    }
  }
}

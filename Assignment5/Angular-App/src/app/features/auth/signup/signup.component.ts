import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, NgForm, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/core/services/auth/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent implements OnInit {
  @ViewChild('signUpNgForm') signUpNgForm!: NgForm;

  signUpForm!: FormGroup;
  showAlert: boolean = false;

  constructor(
    private _authService: AuthenticationService,
    private _formBuilder: FormBuilder,
    private _router: Router
  ) {}
  ngOnInit(): void {
    // Create the form
    // Create the form
    this.signUpForm = this._formBuilder.group({
      name: ['', Validators.required],
      // email: ['', [Validators.required, Validators.email]],
      email: ['', [Validators.required]],
      password: ['', Validators.required],
      company: [''],
      agreements: ['', Validators.requiredTrue],
    });
  }

  /**
   * Sign up
   */
  signUp(): void {
    // Do nothing if the form is invalid
    if (this.signUpForm.invalid) {
      return;
    }

    // Disable the form
    this.signUpForm.disable();

    // Hide the alert
    this.showAlert = false;

    // Sign up
    this._authService.signUp(this.signUpForm.value).subscribe(
      response => {
        if (response.status_code === 200) {
          // Navigate to the confirmation required page
          this._router.navigateByUrl('/confirmation-required');
        } else {
          console.log('error in signup');
        }
      },
      response => {
        // Re-enable the form
        this.signUpForm.enable();

        // Reset the form
        this.signUpNgForm.resetForm();

        // Set the alert
        // this.alert = {
        //     type   : 'error',
        //     message: 'Something went wrong, please try again.'
        // };

        // Show the alert
        this.showAlert = true;
      }
    );
  }
}

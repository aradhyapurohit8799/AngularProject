import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RetailDashboardComponent } from './retail-dashboard/retail-dashboard.component';

const routes: Routes = [
  {
    path: "",
    component: LoginComponent
  },
  {
    path: "retail-dashboard",
    component: RetailDashboardComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

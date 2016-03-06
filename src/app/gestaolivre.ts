import {View, Component} from 'angular2/core';
import {Location, RouteConfig, RouterLink, Router} from 'angular2/router';
import {AuthHttp, JwtHelper} from 'angular2-jwt';

import {Observable} from 'rxjs/Rx';

import {LoggedInRouterOutlet} from './LoggedInOutlet';
import {Home} from './home/home';
import {Login} from './authentication/login';
import {Signup} from './authentication/signup';


@Component({
  selector: 'gestaolivre-app'
})
@View({
  templateUrl: './app/gestaolivre.html',
  directives: [LoggedInRouterOutlet]
})
@RouteConfig([
  { path: '/', redirectTo: ['/Home'] },
  { path: '/home', component: Home, as: 'Home' },
  { path: '/login', component: Login, as: 'Login' },
  { path: '/signup', component: Signup, as: 'Signup' }
])
export class GestaoLivreApp {
  tokenExpires: number;
  constructor(public router: Router, public authHttp: AuthHttp) {
    let timer = Observable.timer(2000, 1000);
    let jwtHelper: JwtHelper = new JwtHelper();
    timer.subscribe(t => {
      var token = jwtHelper.decodeToken(localStorage.getItem('id_token'));
      this.tokenExpires = ((token.exp * 1000) - Number(new Date()));
    });
  }
}

import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { BaseService } from './base.service';

@Injectable({
  providedIn: 'root'
})
export class PlayersService extends BaseService {
  constructor(protected http: HttpClient) {
    super(http);
  }

  // Existing method to fetch player summary
  getPlayerSummary(playerID: number): Observable<any> {
    const endpoint = `${this.baseUrl}/playerSummary/${playerID}`;

    return this.get(endpoint).pipe(map(
      (data: Object) => {
        return {
          endpoint: endpoint,
          apiResponse: data
        };
      },
      error => {
        return error;
      }
    ));
  }

  // New method to fetch search autocomplete results
  searchAutocomplete(term: string): Observable<any> {
    const endpoint = `${this.baseUrl}/searchAutocomplete`;

    // Send the query as a parameter
    let params = new HttpParams().set('query', term);

    return this.http.get(endpoint, { params }).pipe(
      map((data: any) => {
        return data;
      },
      error => {
        return error;
      })
    );
  }
}

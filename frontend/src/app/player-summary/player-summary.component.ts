import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { PlayersService } from '../_services/players.service';
import { debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';
import { Subject } from 'rxjs';

@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
})
export class PlayerSummaryComponent implements OnInit {
  searchTerm = new Subject<string>();  // Input for searching players
  searchResults: any = { players: [], teams: [] };  // Store search results
  playerSummary: any | null = null;  // Store selected player's summary data

  constructor(private playersService: PlayersService, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    // Debounce search input and make API requests
    this.searchTerm.pipe(
      debounceTime(300),  // Wait 300ms after typing
      distinctUntilChanged(),
      switchMap(term => this.playersService.searchAutocomplete(term))  // API call for suggestions
    ).subscribe(results => {
      this.searchResults = results;  // Update search results
      this.cdr.detectChanges();  // Trigger change detection
    });
  }

  // Trigger search on input change
  onSearchChange(event: any) {
    const searchTerm = event.target.value;
    this.searchTerm.next(searchTerm);  // Emit the search term
  }

  // Handle player selection
  onPlayerSelect(player: any): void {
    console.log("Selected player:", player);  // Debug log
    this.loadPlayerSummary(player.id);  // Load summary using player ID
  }

  // Fetch selected player's summary
  loadPlayerSummary(playerID: number): void {
    console.log("Fetching summary for player ID:", playerID);  // Debug log
    this.playersService.getPlayerSummary(playerID).subscribe(data => {
      console.log("Player summary data:", data);  // Debug log for response
      this.playerSummary = data.apiResponse;  // Store player summary from response
      this.cdr.detectChanges();  // Trigger change detection
    }, error => {
      console.log("Error fetching player summary:", error);  // Handle errors
    });
  }

  convertX(locationX: number): number {
    const courtPixelWidth = 400; 
    const courtRealWidth = 50; 
    const pixelsPerFootX = courtPixelWidth / courtRealWidth; 
  
    const centerCourtX = courtPixelWidth / 2; 
    return centerCourtX + (locationX * pixelsPerFootX); 
  }
  
  convertY(locationY: number): number {
    const courtPixelHeight = 400; 
    const courtRealHeight = 23.75; 
    const pixelsPerFootY = courtPixelHeight / courtRealHeight; 
  
    return courtPixelHeight - (locationY * pixelsPerFootY); 
  }
  
  
  
}
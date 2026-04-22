import pygame
import random
import sys

# --- KONFIGURATION & THEME ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60

# Farben (Immersive UI Theme)
BG_COLOR = (15, 23, 42)        # Deep Navy
CELL_BG = (30, 41, 59)         # Slate 800
CELL_BORDER = (71, 85, 105)    # Slate 600
TEXT_COLOR = (255, 255, 255)
CORRECT_COLOR = (16, 185, 129) # Emerald 500
WRONG_PLACE_COLOR = (202, 138, 4) # Yellow 600
INCORRECT_COLOR = (51, 65, 85)   # Slate 700
EMERALD_GLOW = (16, 185, 129, 100)

# Wörterbuch (Auszug)
WORDS = {
    "de": {
        3: ["AAL", "ABO", "AKT", "ALM", "AMT", "ART", "AST", "AUF", "AUS", "BAD", 
    "BAU", "BEI", "BIT", "BOX", "BUH", "EHE", "EIS", "ELF", "ERZ", "FAN", 
    "FAX", "FEE", "GEL", "GEN", "GUT", "HAI", "HOF", "HUT", "ICH", "IHM", 
    "IHN", "IHR", "INN", "IST", "JOB", "KAI", "KID", "KUR", "LAB", "LOB", 
    "LOG", "LOS", "MAI", "MAL", "MAU", "MET", "MIX", "MUT", "NAH", "NEU", 
    "NIE", "NOT", "NUN", "OFT", "OHR", "OST", "RAD", "RAT", "RAU", "REH", 
    "ROH", "ROT", "RUF", "SAU", "SEE", "SET", "SIE", "SKI", "SOL", "TAG", 
    "TAT", "TEE", "TOD", "TON", "TOR", "TOT", "TUN", "UHR", "UND", "UNS", 
    "UWE", "VON", "VOR", "WAL", "WAS", "WEG", "WEM", "WEN", "WER", "WIE", 
    "WIR", "WUT", "ZUG"],
        4: ["HAUS", "BAUM", "GELD", "ZEIT", "BERG", "WIND", "MOND", "HELL", "WARM", "KALT"],
        5: ["APFEL", "BIRNE", "NACHT", "GLÜCK", "LIEBE", "STERN", "STADT", "STUHL", "TISCH"],
        6: ["SOMMER", "WINTER", "HERBST", "FREUND", "SCHULE", "GARTEN", "KAFFEE", "SILBER"],
        7: ["KLAVIER", "FENSTER", "SPIEGEL", "TRINKEN", "GLAUBEN", "TASCHEN", "KONZERT"],
        8: ["COMPUTER", "FLUGZEUG", "KALENDER", "SCHLÜSSE", "ÜBUNG", "ZAUBERER"]
    },
    "en": {
        3: ["THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "ANY", "CAN"],
        4: ["TIME", "YEAR", "MAKE", "GOOD", "SOME", "TAKE", "WANT", "GAME", "LIFE", "BOOK"],
        5: ["WATER", "ABOUT", "OTHER", "WORLD", "WORDS", "MUSIC", "PHONE", "NIGHT", "LIGHT"],
        6: ["SCHOOL", "FAMILY", "FRIEND", "SUMMER", "WINTER", "GARDEN", "BRIGHT", "PLANET"],
        7: ["COLLEGE", "WEATHER", "JOURNEY", "HISTORY", "MORNING", "FREEDOM", "STUDENT"],
        8: ["COMPUTER", "MOUNTAIN", "LANGUAGE", "PROGRESS", "FEEDBACK", "INTERNET"]
    }
}

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Wörtre")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.SysFont("Arial Black", 36)
        self.font_medium = pygame.font.SysFont("Arial", 24, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 14, bold=True)
        
        self.reset_game_state()

    def reset_game_state(self):
        self.language = "de" # Standard
        self.level = 3
        self.total_score = 0
        self.total_attempts = 0
        self.longest_word = ""
        self.state = "START" # START, PLAYING, WON, GAMEOVER
        self.current_word = ""
        self.attempts = []
        self.current_input = ""
        self.max_attempts = 6
        self.message = ""

    def start_level(self, level):
        self.level = level
        word_list = WORDS[self.language].get(level)
        if not word_list:
            self.state = "GAMEOVER"
            return
        self.current_word = random.choice(word_list)
        self.attempts = []
        self.current_input = ""
        self.state = "PLAYING"
        self.message = ""

    def check_word(self, guess):
        secret = self.current_word
        results = [None] * len(secret)
        secret_list = list(secret)
        guess_list = list(guess)

        # 1. Pass: Korrekte Position
        for i in range(len(guess)):
            if guess_list[i] == secret_list[i]:
                results[i] = "correct"
                secret_list[i] = "_"

        # 2. Pass: Falsche Position
        for i in range(len(guess)):
            if results[i] is None:
                if guess_list[i] in secret_list:
                    results[i] = "wrong_place"
                    idx = secret_list.index(guess_list[i])
                    secret_list[idx] = "_"
                else:
                    results[i] = "incorrect"
        return results

    def submit_guess(self):
        if len(self.current_input) != self.level:
            self.message = "Zu kurz!" if self.language == "de" else "Too short!"
            return
        elif self.current_input not in WORDS[self.language][self.level]:
            # Falls ihr ein Wort nutzt, das nicht in der Liste steht, 
            # wird es hier abgelehnt. Das ist gut für die Spielregeln!
            self.message = "Kein Wort!" if self.language == "de" else "Not a word!"
            return
        
        guess = self.current_input
        self.attempts.append(guess)
        
        if guess == self.current_word:
            # Score Berechnung
            base = self.level * 10
            bonus = (self.max_attempts - len(self.attempts)) * 5
            self.total_score += (base + bonus)
            self.total_attempts += len(self.attempts)
            if self.level > len(self.longest_word):
                self.longest_word = self.current_word
            self.state = "WON"
        elif len(self.attempts) >= self.max_attempts:
            self.total_attempts += len(self.attempts)
            self.state = "GAMEOVER"
        else:
            self.current_input = ""
            self.message = ""

    def draw_start_screen(self):
        self.screen.fill(BG_COLOR)
        # Titel
        title_surf = self.font_large.render("WÖRTR E", True, TEXT_COLOR)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH//2, 200))
        self.screen.blit(title_surf, title_rect)
        
        # Untertitel
        sub_surf = self.font_small.render("PROGRESSIVES WORDLE", True, CELL_BORDER)
        sub_rect = sub_surf.get_rect(center=(SCREEN_WIDTH//2, 250))
        self.screen.blit(sub_surf, sub_rect)

        # Buttons
        de_btn = pygame.Rect(SCREEN_WIDTH//2 - 100, 400, 200, 50)
        en_btn = pygame.Rect(SCREEN_WIDTH//2 - 100, 470, 200, 50)
        
        pygame.draw.rect(self.screen, CORRECT_COLOR, de_btn, border_radius=10)
        pygame.draw.rect(self.screen, CELL_BG, en_btn, border_radius=10)
        pygame.draw.rect(self.screen, CELL_BORDER, en_btn, 2, border_radius=10)

        de_txt = self.font_medium.render("DEUTSCH", True, BG_COLOR)
        self.screen.blit(de_txt, de_txt.get_rect(center=de_btn.center))
        
        en_txt = self.font_medium.render("ENGLISH", True, TEXT_COLOR)
        self.screen.blit(en_txt, en_txt.get_rect(center=en_btn.center))

        return de_btn, en_btn

    def draw_grid(self):
        cell_size = 60
        margin = 10
        start_x = (SCREEN_WIDTH - (self.level * (cell_size + margin))) // 2
        start_y = 150

        for row in range(self.max_attempts):
            for col in range(self.level):
                rect = pygame.Rect(start_x + col*(cell_size+margin), start_y + row*(cell_size+margin), cell_size, cell_size)
                
                color = CELL_BG
                border_color = CELL_BORDER
                char = ""

                if row < len(self.attempts):
                    char = self.attempts[row][col]
                    results = self.check_word(self.attempts[row])
                    if results[col] == "correct": color = CORRECT_COLOR
                    elif results[col] == "wrong_place": color = WRONG_PLACE_COLOR
                    else: color = INCORRECT_COLOR
                    border_color = color
                elif row == len(self.attempts):
                    if col < len(self.current_input):
                        char = self.current_input[col]
                    pygame.draw.rect(self.screen, CELL_BG, rect, border_radius=5)
                    border_color = (255, 255, 255) if col == len(self.current_input) else CELL_BORDER
                
                pygame.draw.rect(self.screen, color, rect, border_radius=5)
                pygame.draw.rect(self.screen, border_color, rect, 2, border_radius=5)
                
                if char:
                    char_surf = self.font_medium.render(char, True, TEXT_COLOR)
                    self.screen.blit(char_surf, char_surf.get_rect(center=rect.center))

    def draw_playing_ui(self):
        self.screen.fill(BG_COLOR)
        # Header Info
        header_txt = self.font_small.render(f"LVL {self.level} | {self.language.upper()} | SCORE: {self.total_score}", True, CELL_BORDER)
        self.screen.blit(header_txt, (20, 20))
        
        self.draw_grid()
        
        if self.message:
            msg_surf = self.font_small.render(self.message, True, WRONG_PLACE_COLOR)
            self.screen.blit(msg_surf, msg_surf.get_rect(center=(SCREEN_WIDTH//2, 650)))

    def draw_end_screen(self, title, button_text):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((15, 23, 42, 200))
        self.screen.blit(overlay, (0,0))
        
        # Panel breiter machen (450 statt 300), damit auch lange Wörter wie COMPUTER passen
        panel_width = 450
        panel = pygame.Rect(SCREEN_WIDTH//2 - panel_width//2, SCREEN_HEIGHT//2 - 200, panel_width, 400)
        pygame.draw.rect(self.screen, CELL_BG, panel, border_radius=20)
        pygame.draw.rect(self.screen, CELL_BORDER, panel, 2, border_radius=20)

        t_surf = self.font_large.render(title, True, TEXT_COLOR)
        self.screen.blit(t_surf, t_surf.get_rect(center=(SCREEN_WIDTH//2, panel.top + 50)))
        
        # Wort etwas größer und in Farbe anzeigen
        word_txt = self.font_medium.render(f"Wort: {self.current_word}", True, CORRECT_COLOR)
        self.screen.blit(word_txt, word_txt.get_rect(center=(SCREEN_WIDTH//2, panel.top + 100)))

        stats = [
            f"Punkte: {self.total_score}",
            f"Längstes Wort: {self.longest_word if self.longest_word else '-'}",
            f"Versuche gesamt: {self.total_attempts}"
        ]
        for i, s in enumerate(stats):
            # Prüfen, ob der Text zu breit für die Box ist, sonst kleinere Schrift nutzen
            s_surf = self.font_medium.render(s, True, TEXT_COLOR)
            if s_surf.get_width() > panel_width - 60:
                s_surf = self.font_small.render(s, True, TEXT_COLOR)
            
            self.screen.blit(s_surf, (panel.left + 30, panel.top + 160 + i*45))

        btn = pygame.Rect(SCREEN_WIDTH//2 - 100, panel.bottom - 80, 200, 50)
        pygame.draw.rect(self.screen, CORRECT_COLOR, btn, border_radius=10)
        btn_txt = self.font_medium.render(button_text, True, BG_COLOR)
        self.screen.blit(btn_txt, btn_txt.get_rect(center=btn.center))
        return btn

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "START":
                        de_btn, en_btn = self.draw_start_screen()
                        if de_btn.collidepoint(mouse_pos):
                            self.language = "de"
                            self.start_level(3)
                        elif en_btn.collidepoint(mouse_pos):
                            self.language = "en"
                            self.start_level(3)
                    elif self.state == "WON":
                        btn = self.draw_end_screen("GEWONNEN!", "Nächstes Level")
                        if btn.collidepoint(mouse_pos):
                            self.start_level(self.level + 1)
                    elif self.state == "GAMEOVER":
                        btn = self.draw_end_screen("GAME OVER", " Neustart")
                        if btn.collidepoint(mouse_pos):
                            self.reset_game_state()

                if event.type == pygame.KEYDOWN and self.state == "PLAYING":
                    if event.key == pygame.K_RETURN:
                        self.submit_guess()
                    elif event.key == pygame.K_BACKSPACE:
                        self.current_input = self.current_input[:-1]
                    elif len(self.current_input) < self.level:
                        char = event.unicode.upper()
                        if char.isalpha():
                            self.current_input += char

            # Rendering
            if self.state == "START":
                self.draw_start_screen()
            elif self.state == "PLAYING":
                self.draw_playing_ui()
            elif self.state == "WON":
                self.draw_playing_ui()
                self.draw_end_screen("GEWONNEN!", "WEITER")
            elif self.state == "GAMEOVER":
                self.draw_playing_ui()
                self.draw_end_screen("GAME OVER", "NEUSTART")

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()

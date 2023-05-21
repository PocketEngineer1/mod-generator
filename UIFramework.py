import pygame

pygame.init()
pygame.font.init()

class Element:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

#region RadioButton
class RadioButton(Element):
    def __init__(self, x, y, size=20, color=(0, 0, 0), selected=False, group=None, click_handler=None, label='', font=None, font_size=20):
        super().__init__(x, y, size, size)  # Call the __init__ method of the Element class
        self.color = color
        self.selected = selected
        self.group = group
        self.click_handler = click_handler
        self.label = label
        self.font = pygame.font.Font(font, font_size)
        
        # If this button is part of a group, register it
        if group is not None:
            group.add_button(self)

    def draw(self, surface):
        # Draw the button outline
        pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 2, 3)
        # If selected, draw a filled circle in the center
        if self.selected:
            pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 4)
        
        if self.label:
            label_text = self.font.render(self.label, True, self.color)
            label_rect = label_text.get_rect(left=self.rect.right + 10, centery=self.rect.centery)
            surface.blit(label_text, label_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.selected = True
                if self.group is not None:
                    self.group.deselect_other_buttons(self)
                if self.click_handler is not None:
                    self.click_handler()

    def deselect(self):
        self.selected = False

class RadioButtonGroup:
    def __init__(self):
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def deselect_other_buttons(self, selected_button):
        for button in self.buttons:
            if button is not selected_button:
                button.deselect()
#endregion

class Checkbox(Element):
    def __init__(self, x, y, size=20, label='', font_size=20, checked=False, color=(0, 0, 0), check_color=(0, 0, 0), font=None, group=None):
        super().__init__(x, y, size, size)
        self.label = label
        self.font = pygame.font.Font(font, font_size)
        self.checked = checked
        self.color = color
        self.check_color = check_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        if self.checked:
            pygame.draw.line(surface, self.check_color, (self.rect.left + 5, self.rect.centery), (self.rect.centerx, self.rect.bottom - 5), 2)
            pygame.draw.line(surface, self.check_color, (self.rect.centerx, self.rect.bottom - 5), (self.rect.right - 5, self.rect.top + 5), 2)

        if self.label:
            label_text = self.font.render(self.label, True, self.color)
            label_rect = label_text.get_rect(left=self.rect.right + 10, centery=self.rect.centery)
            surface.blit(label_text, label_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked
  
    def get_checked(self):
        return self.checked

class Rectangle(Element):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def handle_event(self, event):
        pass

class Circle(Element):
    def __init__(self, x, y, width, height, radius, color):
        super().__init__(x, y, width, height)
        self.color = color
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.radius)

    def handle_event(self, event):
        pass

class Button(Element):
    def __init__(self, x, y, width, height, color=(255, 255, 0), text='', text_color=(255, 0, 0), font_size=20, click_handler=None, disabled=False, font=None):
        super().__init__(x, y, width, height)
        self.color = color
        self.text_color = text_color
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.click_handler = click_handler
        self.disabled = disabled

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text != '':
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.disabled:
                if self.rect.collidepoint(event.pos) and event.button == 1:
                    if self.click_handler is not None:
                        self.click_handler()

class Text(Element):
    def __init__(self, x, y, text, font_size=20, color=(0, 0, 0), font=None):
        super().__init__(x, y, font_size, len([*text]) * font_size)  # Call the __init__ method of the Element class
        self.text = text
        self.color = color
        self.font = pygame.font.Font(font, font_size)
        self.height = font_size + 2

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.rect.x, self.rect.x))

    def handle_event(self, event):
        pass
    
class UI:
    def __init__(self, width, height, title, background_color=(255, 255, 255)):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = background_color
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.elements = []

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for element in self.elements:
                    element.handle_event(event)
 
            self.screen.fill(self.background_color)
            for element in self.elements:
                element.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def add_element(self, element):
        self.elements.append(element)

    def clear_elements(self):
        self.elements = []

import pygame, xmltodict
from ast import literal_eval as make_tuple

from functions import *

pygame.init()
pygame.font.init()

class Element:
    def __init__(self, name, x, y, width, height, group, enabled=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.enabled = enabled
        self.name = name
        
        if group is not None:
            group.add_element(self)

    def SetPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

class ElementGroup:
    def __init__(self, name):
        self.elements = []
        self.radio_button_groups = []
        self.enabled = True
        self.name = name

    def add_element(self, element):
        self.elements.append(element)

    def disable(self):
        for element in self.elements:
            element.enabled = False
        self.enabled = False

    def enable(self):
        for element in self.elements:
            element.enabled = True
        self.enabled = True

    def add_element(self, element):
        self.elements.append(element)

    def clear_elements(self):
        self.elements = []
    
    def get_element_by_name(self, name):
        for i in self.elements:
            if i.name == name:
                return i
        Log('Invalid element name', 'ERROR')
    
    def delete_element_by_name(self, name):
        j = 0
        for i in self.elements:
            j += 1
            if i.name == name:
                del self.elements[i]
        Log('Invalid element name', 'ERROR')
    
    def add_radio_button_group(self, radio_button_group):
        self.radio_button_groups.append(radio_button_group)

    def clear_radio_button_groups(self):
        self.radio_button_groups = []
    
    def get_radio_button_group_by_name(self, name):
        for i in self.radio_button_groups:
            if i.name == name:
                return i
        Log('Invalid radio_button_group name', 'ERROR')
    
    def delete_radio_button_group_by_name(self, name):
        j = 0
        for i in self.radio_button_groups:
            j += 1
            if i.name == name:
                del self.radio_button_groups[i]
        Log('Invalid radio button group name', 'ERROR')

class TextInput(Element):
    def __init__(self, name, x, y, width, height, group=None, font_size=20, placeholder='', on_change=None, placeholder_color=(128, 128, 128), text_color=(0, 0, 0), active_color=(0, 0, 255), inactive_color=(128, 128, 128), font=None):
        super().__init__(name, x, y, width, height, group)
        self.text = ''
        self.font = pygame.font.Font(font, font_size)
        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.text_color = text_color
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.active = False
        self.on_change = on_change

    def draw(self, surface):
        # Draw the text input box
        pygame.draw.rect(surface, self.active_color if self.active else self.inactive_color, self.rect, 2)

        # Draw the text if it exists
        if self.text != '':
            text_surface = self.font.render(self.text, True, self.text_color)
            surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        # Draw the placeholder text if the input is empty
        else:
            placeholder_surface = self.font.render(self.placeholder, True, self.placeholder_color)
            surface.blit(placeholder_surface, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle the active state of the input if clicked on
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Update the text color based on the active state
            self.text_color = (0, 0, 0) if self.active else (128, 128, 128)
        elif event.type == pygame.KEYDOWN:
            # Add characters to the input text if active
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Call the on_change function if it exists
                if self.on_change is not None:
                    self.on_change(self.text)

#region RadioButton
class RadioButton(Element):
    def __init__(self, name, x, y, size=20, color=(0, 0, 0), selected=False, button_group=None, group=None, click_handler=None, label='', font=None, font_size=20):
        super().__init__(name, x, y, size, size, group)
        self.color = color
        self.selected = selected
        self.button_group = button_group
        self.click_handler = click_handler
        self.label = label
        self.font = pygame.font.Font(font, font_size)
        
        if button_group is not None:
            button_group.add_button(self)

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
                if self.button_group is not None:
                    self.button_group.deselect_other_buttons(self)
                if self.click_handler is not None:
                    self.click_handler()

    def deselect(self):
        self.selected = False

class RadioButtonGroup:
    def __init__(self, name):
        self.buttons = []
        self.name = name

    def add_button(self, button):
        self.buttons.append(button)

    def deselect_other_buttons(self, selected_button):
        for button in self.buttons:
            if button is not selected_button:
                button.deselect()
#endregion

class Checkbox(Element):
    def __init__(self, name, x, y, size=20, label='', font_size=20, checked=False, color=(0, 0, 0), check_color=(0, 0, 0), font=None, group=None):
        super().__init__(name, x, y, size, size, group)
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
    def __init__(self, name, x, y, width, height, color=(0,0,0), group=None):
        super().__init__(name, x, y, width, height, group)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def handle_event(self, event):
        pass

class Image(Element):
    def __init__(self, name, x, y, image_path, group=None, scale=None):
        self.image = pygame.image.load(image_path)
        super().__init__(name, x, y, self.image.get_width(), self.image.get_height(), group)
        self.image_path = image_path
        self.scale = scale

    def draw(self, surface):
        if self.scale is not None:
            self.image = pygame.transform.scale(self.image, (self.scale, self.scale))

        surface.blit(self.image, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        pass

class Circle(Element):
    def __init__(self, name, x, y, radius, color=(0,0,0), group=None):
        super().__init__(name, x, y, radius * 2, radius * 2, group)
        self.color = color
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.radius)

    def handle_event(self, event):
        pass

class Ellipse(Element):
    def __init__(self, name, x, y, width, height, color=(0, 0, 0), group=None):
        super().__init__(name, x, y, width, height, group)
        self.color = color

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

    def handle_event(self, event):
        pass

class Line(Element):
    def __init__(self, name, start, end, color=(0, 0, 0), thickness=1, group=None):
        super().__init__(name, start[0], start[1], abs(start[0] - start[1]), abs(end[0] - end[1]), group)
        self.color = color
        self.start = start
        self.end = end
        self.thickness = thickness

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.start, self.end, self.thickness)

    def handle_event(self, event):
        pass

class Button(Element):
    def __init__(self, name, x, y, width, height, group=None, color=(200, 200, 200), text='', text_color=(0, 0, 0), font_size=20, click_handler=None, disabled=False, font=None):
        super().__init__(name, x, y, width, height, group)
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
    def __init__(self, name, x, y, text, font_size=20, color=(0, 0, 0), font=None, group=None):
        super().__init__(name, x, y, font_size, len([*text]) * font_size, group)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(font, font_size)
        self.height = font_size + 2

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.rect.x, self.rect.y))

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
        self.groups = []

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for element in self.elements:
                    if element.enabled:
                        element.handle_event(event)
 
            self.screen.fill(self.background_color)
            for element in self.elements:
                if element.enabled:
                    element.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def add_element(self, element):
        self.elements.append(element)

    def clear_elements(self):
        self.elements = []
    
    def get_element_by_name(self, name):
        for i in self.elements:
            if i.name == name:
                return i
        Log('Invalid element name', 'ERROR')
    
    def delete_element_by_name(self, name):
        j = 0
        for i in self.elements:
            j += 1
            if i.name == name:
                del self.elements[i]
        Log('Invalid element name', 'ERROR')

    def add_group(self, group):
        self.groups.append(group)

    def clear_groups(self):
        self.groups = []
    
    def get_group_by_name(self, name):
        for i in self.groups:
            if i.name == name:
                return i
        Log('Invalid group name', 'ERROR')
    
    def delete_group_by_name(self, name):
        j = 0
        for i in self.groups:
            j += 1
            if i.name == name:
                del self.groups[i]
        Log('Invalid group name', 'ERROR')

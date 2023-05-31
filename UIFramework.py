import pygame, time

from functions import *

pygame.init()
pygame.font.init()

class Element:
    def __init__(self, name, x, y, width, height, group, active=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.active = active
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
        self.active = True
        self.name = name

    def add_element(self, element):
        self.elements.append(element)

    def disable(self):
        for element in self.elements:
            element.active = False
        self.active = False

    def enable(self):
        for element in self.elements:
            element.active = True
        self.active = True

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
        for i in self.elements:
            if i.name == name:
                self.elements.remove(i)
                return
        Log('Invalid element name', 'ERROR')
    
    def draw_elements(self, surface):
        for i in self.elements:
            i.draw(surface)

    def heandle_events(self, event):
        for i in self.elements:
            i.handle_event(event)

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
        self.active_self = False
        self.on_change = on_change

    def draw(self, surface):
        # Draw the text input box
        pygame.draw.rect(surface, self.active_color if self.active_self else self.inactive_color, self.rect, 2)

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
                self.active_self = not self.active_self
            else:
                self.active_self = False
            # Update the text color based on the active state
            self.text_color = (0, 0, 0) if self.active_self else (128, 128, 128)
        elif event.type == pygame.KEYDOWN:
            # Add characters to the input text if active
            if self.active_self:
                if event.key == pygame.K_RETURN:
                    self.active_self = False
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

#region Non functional
# class ScrollArea(Element):
#     def __init__(self, name, x, y, width, height, scroll_speed=5, group=None):
#         super().__init__(name, x, y, width, height, group)
#         self.scroll_y = 0
#         self.scroll_speed = scroll_speed
#         self.content_height = self.rect.height
#         self.visible_area_height = self.rect.height
#         self.elements = []

#     def draw(self, surface):
#         for i, item in enumerate(self.elements):
#             if i * 35 > self.scroll_y + self.visible_area_height:
#                 # Skip drawing items below the visible area
#                 break
#             if (i + 1) * 35 >= self.scroll_y:
#                 # Only draw items that are partially or fully visible
#                 item_y = (i * 35) - self.scroll_y
#                 # Draw your file display elements here using the item_y as the y-coordinate
#                 item.rect.y = item_y
#                 item.draw(surface)

#     def handle_event(self, event):
#         if event.type == pygame.KEYDOWN:
#             keys = pygame.key.get_pressed()
#             if keys[pygame.K_UP]:
#                 self.scroll_y += self.scroll_speed
#             if keys[pygame.K_DOWN]:
#                 self.scroll_y -= self.scroll_speed

#             # Clamp scroll position within the content range
#             self.max_scroll_y = self.content_height - self.visible_area_height
#             self.scroll_y = max(0, min(self.scroll_y, self.max_scroll_y))
    
#     def add_elements(self, elements):
#         self.elements = elements
#endregion

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
    def __init__(self, name, x, y, width, height, group=None, color=(200, 200, 200), text='', disabled_text_color=(128, 128, 128), text_color=(0, 0, 0), font_size=20, click_handler=None, enabled=True, font=None):
        super().__init__(name, x, y, width, height, group)
        self.color = color
        self.text_color = text_color
        self.disabled_text_color = disabled_text_color
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.click_handler = click_handler
        self.enabled = enabled

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text != '':
            if self.enabled:
                text_surface = self.font.render(self.text, True, self.text_color)
            else:
                text_surface = self.font.render(self.text, True, self.disabled_text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.enabled:
                if self.rect.collidepoint(event.pos) and event.button == 1:
                    if self.click_handler is not None:
                        self.click_handler()
    
    def set_enabled(self, enabled):
        self.enabled = enabled

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

#region Tabs
class Tab(Element):
    def __init__(self, name, x, y, width, height, tab_group, group, global_group=None, color=(200, 200, 200), text='', disabled_text_color=(128, 128, 128), text_color=(0, 0, 0), font_size=20, enabled=True, font=None):
        super().__init__(name, x, y, width, height, global_group)
        self.color = color
        self.text_color = text_color
        self.disabled_text_color = disabled_text_color
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.enabled = enabled
        self.group = group
        self.tab_group = tab_group
        tab_group.add_tab(self)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text != '':
            if self.enabled:
                text_surface = self.font.render(self.text, True, self.text_color)
            else:
                text_surface = self.font.render(self.text, True, self.disabled_text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def click_handler(self):
        self.tab_group.select_tab_handler(self)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.enabled:
                if self.rect.collidepoint(event.pos) and event.button == 1:
                    self.click_handler()
    
    def set_enabled(self, enabled):
        self.enabled = enabled

class TabGroup:
    def __init__(self):
        self.tabs = []
        self.groups = []

    def add_tab(self, tab):
        self.tabs.append(tab)

    def add_group(self, group):
        self.groups.append(group)

    def select_tab_handler(self, selected_tab):
        selected_tab.set_enabled(False)
        for tab in self.tabs:
            if tab is not selected_tab:
                tab.set_enabled(True)
    
        selected_tab.group.enable()
        for group in self.groups:
            if group is not selected_tab.group:
                group.disable()
#endregion

class UI:
    def __init__(self, width, height, title, handle_elements_outside_of_group=True, background_color=(255, 255, 255)):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = background_color
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.elements = []
        self.groups = []
        self.handle_elements_outside_of_group = handle_elements_outside_of_group
        self.waiting = False
        self.set_waiting(self.waiting)

    def run(self):
        running = True
        while running:
            #region cursor
            if self.waiting != True:
                cursor_pos = pygame.mouse.get_pos()
                cursor_on_element = False
                element_object = None
                for element in self.elements:
                    if element.rect.collidepoint(cursor_pos):
                        cursor_on_element = True
                        element_object = element
                        break

                if cursor_on_element:
                    if element_object is not None:
                        if element_object.active:
                            if element_object.__class__.__name__ == 'Button' or element_object.__class__.__name__ == 'Tab':
                                if element_object.enabled:
                                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                            elif element_object.__class__.__name__ == 'Checkbox' or element_object.__class__.__name__ == 'RadioButton':
                                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                            elif element_object.__class__.__name__ == 'TextInput':
                                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
                            else:
                                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            #endregion

            if self.waiting != True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if self.handle_elements_outside_of_group:
                        for element in self.elements:
                            if element.active:
                                element.handle_event(event)
                    else:
                        for group in self.groups:
                            if group.active:
                                group.handle_event(event)
 
            self.screen.fill(self.background_color)
            if self.handle_elements_outside_of_group:
                for element in self.elements:
                    if element.active:
                        element.draw(self.screen)
            else:
                for group in self.groups:
                    if group.active:
                        group.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
    
    def set_waiting(self, waiting: bool):
        self.waiting = waiting
        if waiting:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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
        for i in self.elements:
            if i.name == name:
                self.elements.remove(i)
                return
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

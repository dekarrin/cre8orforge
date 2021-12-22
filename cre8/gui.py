import traceback

from .activities import Jobs, Outlets
from .engine import Engine, RulesViolationError
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

from typing import Tuple, Optional, Union, Callable, Any

Numeric = Union[int, float, str]


class Counter(tk.Frame):
    """
    Counter component that can track its own value. Has increment and decrement buttons, or user can directly
    edit the value. Arranged in a horizontal structure such as "[-] [FIELD] [+]".
    
    This component is for int values. For float values, use DoubleCounter.

    To get the field that accepts input, use the 'field' attribute. In general it is better to use the
    get() and set() methods on this component though.
    """
    def __init__(self, master, value: Numeric = 0, inc_amount: Numeric = 1):
        super().__init__(master=master)
        
        self.increment_amount = inc_amount

        self._var = tk.StringVar()
        self._last_valid = str(value)

        self._dec_button = tk.Button(self, text="-", command=self.decrement)
        self._dec_button.pack(fill=tk.NONE, side=tk.LEFT)

        self.field = tk.Entry(self, textvariable=self._var)
        self.field.pack(fill=tk.X, side=tk.LEFT)

        self._inc_button = tk.Button(self, text="+", command=self.increment)
        self._inc_button.pack(fill=tk.NONE, side=tk.LEFT)
        
        if value is not None:
            self.set(value)

    def bind_change(self, callback):
        self._var.trace('w', callback)

    def disable(self):
        """
        Set state of all buttons to disabled. Does not allow text to be updated after this, so be sure
        to update text before calling disable.
        """
        self.field.config(state=tk.DISABLED)
        self._inc_button.config(state=tk.DISABLED)
        self._dec_button.config(state=tk.DISABLED)

    def enable(self):
        """
        Set state of all buttons to enabled.
        """
        self.field.config(state=tk.NORMAL)
        self._inc_button.config(state=tk.NORMAL)
        self._dec_button.config(state=tk.NORMAL)
            
    def reset(self):
        """
        Reset the counter to the last valid value it contained, discarding the current
        contents.
        """
        self._var.set(self._last_valid)

    def set(self, value: Numeric):
        """
        Set a new value for the counter.

        :param value: The new value.
        """
        str_val = str(value)
        
        try:
            int(str_val)
            self._last_valid = str(value)
        except ValueError:
            # just dont store it as the last valid value
            pass
        
        self._var.set(str_val)

    def get(self) -> Optional[int]:
        """
        Get the current value of the counter. This will be an int
        if it currently contains a valid numerical value, or None
        if there is not a valid numerical value.
        """
        str_val = self._var.get()
        try:
            val = int(str_val)
            return val
        except ValueError:
            return None

    def decrement(self):
        """
        Decrease the current value by 1. If it is not currently a
        valid value, it is set to the last valid value it was first.
        """
        if self.get() is None:
            self.reset()
        
        self.set(self.get() - self.increment_amount)

    def increment(self):
        """
        Increase the current value by 1.
        """
        old_val = self.get()
        
        if old_val is None:
            self.reset()
            old_val = self.get()
        
        new_val = old_val + self.increment_amount
        self.set(new_val)
        
        
class DoubleCounter(Counter):
    def __init__(self, master, value: Numeric = 0.0, inc_amount: Numeric = 1.0, precision: float = 0.1):
        precision_power = math.log10(precision)
        if not precision_power.is_integer() or precision_power > 0:
            raise ValueError("precision must be given in negative powers of 10, such as 0.1, 0.001, or 0.00001")
        if precision_power == 0:
            raise ValueError("precision of 1 is equivalent to Counter; use that instead")
        self.precision = precision
        
        # precision will get used in set() which is called by super.ctor
        # so make sure to call ctor after precision is setup
        super().__init__(master, value, inc_amount)
        
    def set(self, value: Numeric):
        """
        Set a new value for the counter.

        :param value: The new value.
        """
        str_val = str(value)

        format_precision = abs(int(math.log10(self.precision)))

        try:
            typed_val = float(value)
            str_val = '{1:.{0}f}'.format(format_precision, typed_val)
            self._last_valid = str_val
        except ValueError:
            # just dont store it as the last valid value
            pass

        self._var.set(str_val)

    def get(self) -> Optional[float]:
        """
        Get the current value of the counter. This will be a float
        if it currently contains a valid numerical value, or None
        if there is not a valid numerical value in it.
        """
        str_val = self._var.get()
        try:
            val = float(str_val)
            return val
        except ValueError:
            return None


class ActivitiesOptionsMenu(tk.OptionMenu):
    def __init__(self, master):
        self._options_list = list()
        self._init_options()
        
        self._var = tk.StringVar()
        self._var.set(self._options_list[0])
        
        super().__init__(master, self._var, *self._options_list)
        self.config(width=20)

    def bind_change(self, callback):
        self._var.trace('w', callback)
        
    def value_as_target(self) -> Tuple[Optional[str], int]:
        """
        Read action options that supplies answer to variable and return
        type and index
        """
        val = self._var.get()
        
        idx = -1
        for j in Jobs:
            idx += 1
            if j.name.lower() == val.lower():
                return 'job', idx
        idx = -1
        for o in Outlets:
            idx += 1
            if o.name.lower() == val.lower():
                return 'outlet', idx
        
        return None, 0        
        
    def _init_options(self):
        self._options_list = list()
        self._options_list.append('-- Select Activity --')
        self._options_list.append(' ')
        self._options_list.append('-- Jobs --')
        self._options_list += [j.name for j in Jobs]
        self._options_list.append('-- Outlets --')
        self._options_list += [o.name for o in Outlets]
        
        
class AutomationComponent(tk.Frame):
    """
    Component that lets you enable and disable automation, as well as buy more.
    """
    def __init__(
        self,
        master,
        buy_func: Callable[[str, int], Any],
        enable_func: Callable[[str, int], Any],
        disable_func: Callable[[str, int], Any],
        automated_func: Callable[[str, int], bool],
        text: str,
        **kwargs
    ):
        """
        Create a new AutomationComponent.

        :param master: The master tk.Widget that will be the parent of the component.
        :param buy_func: A callable that accepts a string activity type and activity index
        and purchases the next level of automation for the target specified by them.
        :param enable_func: A callable that accepts a string activity type and activity index
        and enables automation for the target specified by them.
        :param disable_func: A callable that accepts a string activity type and activity index
        and disables automation for the target specified by them.
        :param automated_func: A callable that accepts a string activity type and activity index
        and returns whether automation is on for the target specified by them.
        :param text: What to put as the label for the text.
        """
        super().__init__(master=master, relief=tk.GROOVE, borderwidth=2, **kwargs)
        
        self._buy_callback = buy_func
        self._enable_auto_callback = enable_func
        self._disable_auto_callback = disable_func
        self._is_automated_callback = automated_func
        
        self._label_component = tk.Label(self, text=text)
        self._label_component.pack(side=tk.TOP)

        self._options_component = ActivitiesOptionsMenu(self)
        self._options_component.pack(side=tk.TOP)
        
        self._inputs_frame = tk.Frame(self)
        self._inputs_frame.pack(side=tk.TOP)
        
        self._auto_text = tk.StringVar()
        self._auto_text.set("Automate")

        self._auto_button = tk.Button(master=self._inputs_frame, textvariable=self._auto_text, command=self._auto_pressed)
        self._auto_button.config(state=tk.DISABLED)
        self._auto_button.pack(side=tk.LEFT)

        self._buy_button = tk.Button(master=self._inputs_frame, text="Buy Next", command=self._buy_pressed)
        self._buy_button.config(state=tk.DISABLED)
        self._buy_button.pack(side=tk.LEFT)

        self._options_component.bind_change(self._update_option)
        
    def _buy_pressed(self, *args):
        target_type, target_idx = self._options_component.value_as_target()
        if target_type is None:
            # should never happen
            raise ValueError("can't buy automation without valid selection")
            
        self._buy_callback(target_type, target_idx)
        
    def _auto_pressed(self, *args):
        target_type, target_idx = self._options_component.value_as_target()
        if target_type is None:
            # should never happen
            raise ValueError("can't automate without valid selection")
        
        if self._is_automated_callback(target_type, target_idx):
            self._disable_auto_callback(target_type, target_idx)
        else:
            self._enable_auto_callback(target_type, target_idx)
            
        # now set current button text based on whether automation worked
        if self._is_automated_callback(target_type, target_idx):
            self._auto_text.set("Stop automating")
        else:
            self._auto_text.set("Automate")

    def _update_option(self, *args):
        target_type, target_idx = self._options_component.value_as_target()
        if target_type is None:
            self._auto_text.set("Automate")
            self._auto_button.config(state=tk.DISABLED)
            self._buy_button.config(state=tk.DISABLED)
        else:
            automated = self._is_automated_callback(target_type, target_idx)
            if automated:
                self._auto_text.set("Stop automating")
            else:
                self._auto_text.set("Automate")
                
            self._auto_button.config(state=tk.NORMAL)
            self._buy_button.config(state=tk.NORMAL)


class ActivityValueComponent(tk.Frame):
    """
    Component that allows you to select an item and then set an int-valued property on it. The property is not set
    until an Apply button is pressed. The Apply button is dim until an item is selected and the value
    is not the current value.
    """

    def __init__(
            self,
            master,
            get_value_func: Callable[[str, int], int],
            set_value_func: Callable[[str, int, int], Any],
            text: str,
            **kwargs
    ):
        """
        Create a new ActivityValueComponent.

        :param master: The master tk.Widget that will be the parent of the component.
        :param get_value_func: A callable that accepts a string activity type and activity index
        and returns the current value that the target specified by those two has.
        :param set_value_func: A callable that accepts a string activity type and activity index
        as well as the value to set on that target specified by those two. This will always be passed
        a type-correct valid value; it will not be called if the user has entered invalid (non-int)
        input.
        :param text: What to put as the label for the text.
        """
        super().__init__(master=master, relief=tk.GROOVE, borderwidth=2, **kwargs)

        self._getter_callback = get_value_func
        self._setter_callback = set_value_func

        self._label_component = tk.Label(self, text=text)
        self._label_component.pack(side=tk.TOP)

        self._options_component = ActivitiesOptionsMenu(self)
        self._options_component.pack(side=tk.TOP)

        self._inputs_frame = tk.Frame(self)
        self._inputs_frame.pack(side=tk.TOP)

        self._counter_component = Counter(master=self._inputs_frame, value="")
        self._counter_component.field.config(width=8)
        self._counter_component.disable()
        self._counter_component.pack(side=tk.LEFT)

        self._button_component = tk.Button(master=self._inputs_frame, text="Apply", command=self.apply)
        self._button_component.config(state=tk.DISABLED)
        self._button_component.pack(side=tk.LEFT)

        self._options_component.bind_change(self._update_option)
        self._counter_component.bind_change(self._update_counter)

    def apply(self):
        """
        Apply the current value in the counter to the selected activity.

        Raises an exception if a valid activity is not selected.
        """
        target_type, target_idx = self._options_component.value_as_target()
        if target_type is None:
            raise ValueError("Need to select a valid activity target before applying")

        set_val = self._counter_component.get()
        if set_val is None:
            raise ValueError("Need to specify a valid value before calling applying")

        self._setter_callback(target_type, target_idx, set_val)

    def _update_option(self, *args):
        target_type, target_idx = self._options_component.value_as_target()
        if target_type is None:
            self._counter_component.set("")
            self._counter_component.disable()
            self._button_component.config(state=tk.DISABLED)
        else:
            cur_val = self._getter_callback(target_type, target_idx)
            self._counter_component.enable()
            self._counter_component.set(cur_val)
            self._button_component.config(state=tk.DISABLED)

    def _update_counter(self, *args):
        target_type, target_idx = self._options_component.value_as_target()
        if target_type is None:
            # should never happen, but just return in this case
            return

        set_val = self._counter_component.get()
        if set_val is None:
            self._button_component.config(state=tk.DISABLED)
            return

        cur_val = self._getter_callback(target_type, target_idx)
        if cur_val != set_val:
            self._button_component.config(state=tk.NORMAL)
        else:
            self._button_component.config(state=tk.DISABLED)


class FlowWindow(tk.Toplevel):
    """
    A top-level window with prev and next buttons that shows a flow of information.
    The steps are advanced through when the user clicks the next button, and goes
    back when the user clicks the prev button.
    
    This window looks like the main window of cre8or forge, with a main content
    pane and an output pane. The entry area contains only the next and prev
    buttons.
    
    Once it is created, add all desired steps, then call start() to begin the flow.
    """
    def __init__(self, master, intro_text="Press 'Next' to get started"):
        super().__init__(master)
        
        self._steps = list()
        self._next_button: tk.Button
        self._prev_button: tk.Button
        
        # set to -1 so we can call next() at end of __init__ which will immediately move it to 0.
        self._step_index = -1
        self.add_step(output=intro_text)
        
        self.rowconfigure(0, minsize=300, weight=1)
        self.columnconfigure(0, minsize=400, weight=1)
        self.columnconfigure(1, minsize=200, weight=0)
        self.rowconfigure(1, minsize=100, weight=0)
        
        content_frame, self.main_content = self._create_main_content_frame(self)
        entry_frame, self._prev_button, self._next_button = self._create_entry_frame(self)
        output_frame, self.output = self._create_output_frame(self, 7)
        
        content_frame.grid(row=0, column=0, sticky="nsew")
        entry_frame.grid(row=0, column=1, sticky="nsew")
        output_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        
    def add_step(self, output: Optional[str] = None, content: Optional[str] = None):
        """
        Add a step to the flow. Steps will be displayed to the user in the
        order that they are added.
        
        :param output: What to show in the output pane. Set to None to leave the
        output pane unmodified from any previous text. Set to an empty string to
        erase the output pane of any previous text.
        :param content: What to show in the main content pane. Set to None to
        leave the main content pane unmodified from any previous text. Set to an
        empty string to erase the content pane of any previous text.
        """
        step = {
            'output': '',
            'content': ''
        }
        
        # instead of leaving as None when specified, give it same text
        # as prev step. This will make hitting prev way easier since
        # the entire step chain doesnt need to get replayed just to find
        # out what is empty and what isnt on prev step.
        prev_step = None
        if len(self._steps) > 0:
            prev_step = self._steps[-1]
        
        if output is None:
            if prev_step is not None:
                step['output'] = prev_step['output']
        else:
            step['output'] = str(output)
        
        if content is None:
            if prev_step is not None:
                step['content'] = prev_step['content']
        else:
            step['content'] = str(content)
            
        self._steps.append(step)
        
    def start(self):
        """
        Start flow from the beginning.
        """
        self._step_index = -1
        self.next()
        
    def next(self):
        """
        Show the next step.
        """
        self._step_index += 1
        self._run_current_step()
        
    def prev(self):
        """
        Show the previous step.
        """
        self._step_index -= 1
        self._run_current_step()
        
    def write_output(self, text: str):
        self.output.config(state=tk.NORMAL)
        self.output.delete("0.0", tk.END)
        self.output.insert("0.0", text)
        self.output.config(state=tk.DISABLED)
        
    def write_main_content(self, text: str):
        scroll_top, _ = self.main_content.yview()
        self.main_content.config(state=tk.NORMAL)
        self.main_content.delete("0.0", tk.END)
        self.main_content.insert("0.0", text)
        self.main_content.config(state=tk.DISABLED)
        self.main_content.yview_moveto(scroll_top)
        
    def _run_current_step(self):
        """
        Perform the instructions in the current flow step and set the prev and
        next buttons as enabled or disabled based on the current step index.
        """
        if self._step_index >= len(self._steps):
            self._step_index = len(self._steps) - 1
        if self._step_index < 0:
            self._step_index = 0
            
        step = self._steps[self._step_index]
        
        self.write_output(step['output'])
        self.write_main_content(step['content'])
            
        if self._step_index > 0:
            self._prev_button.config(state=tk.NORMAL)
        else:
            self._prev_button.config(state=tk.DISABLED)
            
        if self._step_index + 1 < len(self._steps):
            self._next_button.config(state=tk.NORMAL)
        else:
            self._next_button.config(state=tk.DISABLED)
        
    def _create_main_content_frame(self, master) -> Tuple[tk.Widget, tk.Text]:
        """
        Return the main content frame with all children configured. Additionally,
        return the Text field that holds the contents of text within the main
        content frame.
        
        The returned frame will not have had its geometry manager set.
        """
        frm_main = tk.Frame(master=master, relief=tk.SUNKEN, borderwidth=3)
        mc_field = tk.Text(master=frm_main)
        mc_scrollbar = ttk.Scrollbar(master=frm_main, command=mc_field.yview)
        mc_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        mc_field['yscrollcommand'] = mc_scrollbar.set
        mc_field.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        
        return frm_main, mc_field
        
    def _create_entry_frame(self, master) -> Tuple[tk.Frame, tk.Button, tk.Button]:
        """
        Return the entry frame with all children configured. Additionally,
        return the previous and next buttons that were created so their state
        can be updated later.
        
        The returned frame will not have had its geometry manager set.
        """
        entry_frame = tk.Frame(master=master)
        
        frm_bot_buttons = tk.Frame(master=entry_frame)
        frm_bot_buttons.pack(side=tk.BOTTOM, fill=tk.X)
        
        next_btn = tk.Button(master=frm_bot_buttons, text="Next ->", command=self.next)
        next_btn.pack(side=tk.RIGHT)
        
        prev_btn = tk.Button(master=frm_bot_buttons, text="<- Prev", command=self.prev)
        prev_btn.pack(side=tk.LEFT)
        
        return entry_frame, prev_btn, next_btn
        
    def _create_output_frame(self, master, output_lines) -> Tuple[tk.Widget, tk.Text]:
        """
        Return the output frame with all children configured. Additionally,
        return the Text field that holds the contents of text within the
        output frame.
        
        The returned frame will not have had its geometry manager set.
        """
        frm = tk.Frame(master=master)
        output = tk.Text(master=frm, height=output_lines, width=103)
        output.config(state=tk.DISABLED)
        output.pack(fill=tk.X)
        return frm, output


class Gui:
    def __init__(self, g: Engine, output_lines: int = 7):
        self.debug_money: Counter
        self.debug_juice: DoubleCounter
        self.debug_seeds: DoubleCounter
        self.debug_ideas: Counter
        
        # Assumes tabs added in this order: 'Play', 'Store', 'Debug'
        
        self.play_entry_notebook_index = 0
        self.store_entry_notebook_index = 1
        self.debug_entry_notebook_index = 2
        
        self.update_main_content = True
        self.g = g
        self.root = tk.Tk()
        self.root.title("Cre8or Forge v0.0a")
        self.root.report_callback_exception = self.on_error
        
        # setup root window config
        self.root.rowconfigure(0, minsize=300, weight=1)
        self.root.columnconfigure(0, minsize=400, weight=1)
        self.root.columnconfigure(1, minsize=200, weight=0)
        self.root.rowconfigure(1, minsize=100, weight=0)
        
        _, self.main_content = self._build_main_content_frame(self.root)
        
        self.entry_frames_notebook = self._build_entry_frames(self.root)
        
        # setup up output frame and store it for later outputting
        _, self.output = self._build_output_frame(self.root, output_lines)

        # do a single update to get window size then set it as the minimum
        # so user cant resize smaller than the elements
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())

    def on_error(self, exc_type, exc_value, exc_traceback):
        if exc_type == KeyboardInterrupt:
            self.root.destroy()
            return

        msg = 'Oh no it crashed glub! Please tell deka! 38O\n\n\n'
        msg += ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        messagebox.showwarning('Error! Glub!', msg)
        
    def run(self):
        self.root.after(0, self._update)
        self.root.mainloop()
        
    def write_output(self, text: str):
        self.output.config(state=tk.NORMAL)
        self.output.delete("0.0", tk.END)
        self.output.insert("0.0", text)
        self.output.config(state=tk.DISABLED)
        
    def write_main_content(self, text: str):
        scroll_top, _ = self.main_content.yview()
        self.main_content.config(state=tk.NORMAL)
        self.main_content.delete("0.0", tk.END)
        self.main_content.insert("0.0", text)
        self.main_content.config(state=tk.DISABLED)
        self.main_content.yview_moveto(scroll_top)
        
    def apply_debug(self):
        money = self.debug_money.get()
        if money is None:
            self.write_output("Money is not set to a valid value")
            return

        juice = self.debug_juice.get()
        if juice is None:
            self.write_output("Juice is not set to a valid value")
            return

        seeds = self.debug_seeds.get()
        if seeds is None:
            self.write_output("Seeds is not set to a valid value")
            return

        ideas = self.debug_ideas.get()
        if ideas is None:
            self.write_output("(i)deas is not set to a valid value")
            return

        self.g.set_state(money=money, juice=juice, seeds=seeds, ideas=ideas)
        self.write_output("Applied debug settings to the current game")
        self.entry_frames_notebook.select(0)

    @property
    def in_debug_mode(self) -> bool:
        idx = self.entry_frames_notebook.index(tk.CURRENT)
        return idx == self.debug_entry_notebook_index
    
    @property
    def in_store_mode(self) -> bool:
        idx = self.entry_frames_notebook.index(tk.CURRENT)
        return idx == self.store_entry_notebook_index
    
    @property
    def in_play_mode(self) -> bool:
        idx = self.entry_frames_notebook.index(tk.CURRENT)
        return idx == self.play_entry_notebook_index
        
    def tutorial(self):
        """
        Launch the tutorial window.
        """
        tut = FlowWindow(self.root)
        tut.title("Tutorial")
        tut.add_step(output="1 - This is the first step", content="ERASE THIS")
        tut.add_step(output="2 - This step leaves content pane alone")
        tut.add_step(output="3 - Now this step erases the main content", content="")
        tut.add_step(content="4 - Update the content without updating the others")
        tut.add_step(content="5 - Wipe content")
        tut.start()
        
        # make it modal
        tut.focus_set()
        tut.grab_set()
        tut.transient(self.root)
        tut.wait_window(tut)
        
    def _update(self):
        if self.in_debug_mode:
            self.write_main_content("In debug mode. Switch back to the game to resume display")
            self.update_main_content = True
        else:
            self.g.update()
            
            # set debug mode stats so it is correct when user swaps to it
            self.debug_money.set(self.g.get_state('money'))
            self.debug_juice.set(self.g.get_state('juice'))
            self.debug_seeds.set(self.g.get_state('seeds'))
            self.debug_ideas.set(self.g.get_state('ideas'))
        
            if self.in_play_mode:
                self.write_main_content(self.g.status())
                self.update_main_content = True  # this must be here in case a swap to store mode occurs
            elif self.in_store_mode:
                if self.update_main_content:
                    self.write_main_content(self.g.show_store())
                    self.update_main_content = False
            else:
                raise ValueError("Should never happen")
        
        self.root.after(100, self._update)

    # noinspection PyMethodMayBeStatic
    def _build_main_content_frame(self, master) -> Tuple[tk.Widget, tk.Text]:
        """
        Return the fully-configured main content frame with geometry manager
        already set. Additionally, return the Text field that holds the contents
        of text within the main content frame.
        """
        frm_main = tk.Frame(master=master, relief=tk.SUNKEN, borderwidth=3)
        frm_main.grid(row=0, column=0, sticky="nsew")
        mc_field = tk.Text(master=frm_main)
        mc_scrollbar = ttk.Scrollbar(master=frm_main, command=mc_field.yview)
        mc_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        mc_field['yscrollcommand'] = mc_scrollbar.set
        mc_field.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        
        return frm_main, mc_field
        
    def _build_entry_frames(self, master) -> ttk.Notebook:
        entry_frames = ttk.Notebook(master)
        entry_frames.grid(row=0, column=1, sticky="nsew")
        main_entry_frame = self._build_main_entry_frame(entry_frames)
        store_entry_frame = self._build_store_entry_frame(entry_frames)
        debug_entry_frame = self._build_debug_entry_frame(entry_frames)

        entry_frames.add(main_entry_frame, text="Play")
        entry_frames.add(store_entry_frame, text="Store")
        # ensure debug is always the last entry added
        entry_frames.add(debug_entry_frame, text="Debug")
        return entry_frames
        
    def _build_main_entry_frame(self, master) -> tk.Frame:
        """
        Return the fully-configured and packed main entry frame.
        """
        main_entry_frame = tk.Frame(master=master)
        main_entry_frame.pack(fill=tk.BOTH, expand=True)
        self._build_click_component(main_entry_frame)
        self._build_instances_component(main_entry_frame)
        self._build_automation_component(main_entry_frame)
        
        frm_bot_buttons = tk.Frame(master=main_entry_frame)
        frm_bot_buttons.pack(side=tk.BOTTOM, fill=tk.X)
        
        def meditate():
            msg = "Are you sure you want to meditate on your artistic ventures?\n\n"
            msg += "This will sprout Seeds into (i)deas, but it will also RESET ALL PROGRESS except for boosts, automations, and ideas."
            
            if not messagebox.askyesno("Confirm Prestige", msg):
                return
            
            try:
                msg = self.g.prestige()
            except RulesViolationError as e:
                self.write_output(str(e))
                return
                
            self.write_output(msg)
        
        med_btn = tk.Button(master=frm_bot_buttons, text="Medidate", command=meditate)
        med_btn.pack(side=tk.RIGHT)
        tut_btn = tk.Button(master=frm_bot_buttons, text="Tutorial", command=self.tutorial)
        tut_btn.pack(side=tk.LEFT)
        
        return main_entry_frame
        
    def _build_click_component(self, master) -> tk.Frame:
        """
        Return the fully-configured and packed click component frame.
        """
        frm_component = tk.Frame(master=master)
        frm_component.pack(side=tk.TOP, fill=tk.X)
        
        opts_menu = ActivitiesOptionsMenu(frm_component)
        opts_menu.pack(side=tk.LEFT)
        
        def do_click():
            target_type, target_idx = opts_menu.value_as_target()
            if target_type is None:
                self.write_output("Select a valid option first")
                return
            
            try:
                msg = self.g.click(target_type, target_idx)
            except RulesViolationError as ex:
                self.write_output(str(ex))
                return
            
            self.write_output(msg)

        entry_click_lbl = tk.Button(frm_component, text="Click!", command=do_click)
        entry_click_lbl.pack(side=tk.RIGHT)
        return frm_component

    def _build_buy_component(self, master) -> tk.Frame:
        """
        Return the fully-configured and packed buy component frame.
        """
        frm_component = tk.Frame(master=master)
        frm_component.pack(side=tk.TOP, fill=tk.X)
        
        opts_menu = ActivitiesOptionsMenu(frm_component)
        opts_menu.pack(side=tk.LEFT)
        
        def do_buy():
            target_type, target_idx = opts_menu.value_as_target()
            if target_type is None:
                self.write_output("Select a valid option first")
                return
            
            try:
                msg = self.g.buy('instance', target_type, target_idx)
            except RulesViolationError as ex:
                self.write_output(str(ex))
                return
            
            self.write_output(msg)

        entry_click_lbl = tk.Button(frm_component, text="Buy", command=do_buy)
        entry_click_lbl.pack(side=tk.RIGHT)
        return frm_component

    def _build_instances_component(self, master) -> tk.Frame:
        """
        Return the fully-configured and packed activate/deactivate component frame.
        """
        def set_instances(target_type, target_idx, value):
            if value < 0:
                self.write_output("You can't set the number of active instances to less than 0!")
                return

            cur_val = self.g.get_active_count(target_type, target_idx)
            diff = value - cur_val

            try:
                if diff < 0:
                    self.g.deactivate('instance', target_type, target_idx, amount=abs(diff))
                else:
                    self.g.activate('instance', target_type, target_idx, amount=diff)
            except RulesViolationError as e:
                self.write_output(str(e))
                
            total_active = self.g.get_active_count(target_type, target_idx)
            act_name = 'NOTSET'
            if target_type == 'job':
                act_name = Jobs[target_idx].name
            elif target_type == 'outlet':
                act_name = Outlets[target_idx].name
                
            s = 's'
            to_be = 'are'
            if total_active == 1:
                s = ''
                to_be = 'is'
            
            self.write_output("{:d} instance{:s} of {:s} {:s} now active.".format(total_active, s, act_name, to_be))

        comp = ActivityValueComponent(master, self.g.get_active_count, set_instances, "Active Instances")
        comp.pack(side=tk.TOP, fill=tk.X, padx=1, pady=1)
        return comp
    
    def _build_automation_component(self, master) -> tk.Frame:
        """
        Return the fully-configured and packed automation component frame.
        """
        
        def do_buy_auto(target_type, target_idx):
            try:
                msg = self.g.buy('automation', target_type, target_idx)
            except RulesViolationError as ex:
                self.write_output(str(ex))
                return
            
            self.write_output(msg)
            
        def do_activate_auto(target_type, target_idx):
            try:
                msg = self.g.activate('automation', target_type, target_idx)
            except RulesViolationError as ex:
                self.write_output(str(ex))
                return
            
            self.write_output(msg)
            
        def do_deactivate_auto(target_type, target_idx):
            try:
                msg = self.g.deactivate('automation', target_type, target_idx)
            except RulesViolationError as ex:
                self.write_output(str(ex))
                return
            
            self.write_output(msg)
        
        comp = AutomationComponent(
            master,
            buy_func=do_buy_auto,
            enable_func=do_activate_auto,
            disable_func=do_deactivate_auto,
            automated_func=self.g.get_automated,
            text="Automations"
        )
        comp.pack(side=tk.TOP, fill=tk.X, padx=1, pady=1)
        return comp
        
    def _build_store_entry_frame(self, master) -> tk.Frame:
        """
        Return the fully-configured and packed main entry frame.
        """
        store_entry_frame = tk.Frame(master=master)
        store_entry_frame.pack(fill=tk.BOTH, expand=True)
        self._build_buy_component(store_entry_frame)
        return store_entry_frame
        
    def _build_debug_entry_frame(self, master) -> tk.Frame:
        """
        Return the fully-configured and packed debug entry frame.
        """
        debug_entry_frame = tk.Frame(master=master)
        debug_entry_frame.pack(fill=tk.BOTH, expand=True)
        debug_entry_frame.columnconfigure(0, minsize=50, weight=0)
        debug_entry_frame.columnconfigure(1, weight=1)
        
        lbl_debug_money = tk.Label(debug_entry_frame, text="Money:")
        lbl_debug_money.grid(row=0, column=0)
        self.debug_money = Counter(master=debug_entry_frame)
        self.debug_money.grid(row=0, column=1)
        
        lbl_debug_juice = tk.Label(debug_entry_frame, text="Juice:")
        lbl_debug_juice.grid(row=1, column=0)
        self.debug_juice = DoubleCounter(debug_entry_frame, inc_amount=0.01, precision=0.0001)
        self.debug_juice.grid(row=1, column=1)
        
        lbl_debug_seeds = tk.Label(debug_entry_frame, text="Seeds:")
        lbl_debug_seeds.grid(row=2, column=0)
        self.debug_seeds = DoubleCounter(debug_entry_frame, inc_amount=0.01, precision=0.000001)
        self.debug_seeds.grid(row=2, column=1)
        
        lbl_debug_ideas = tk.Label(debug_entry_frame, text="(i)deas:")
        lbl_debug_ideas.grid(row=3, column=0)
        self.debug_ideas = Counter(debug_entry_frame)
        self.debug_ideas.grid(row=3, column=1)
        
        btn_apply = tk.Button(debug_entry_frame, text="Apply", command=self.apply_debug)
        btn_apply.grid(row=5, column=0)
        return debug_entry_frame

    # noinspection PyMethodMayBeStatic
    def _build_output_frame(self, master, output_lines) -> Tuple[tk.Widget, tk.Text]:
        """
        Return the fully-configured output frame with geometry manager
        already set. Additionally, return the Text field that holds the contents
        of text within the output frame.
        """
        frm = tk.Frame(master=master)
        frm.grid(row=1, column=0, columnspan=2, sticky="nsew")
        output = tk.Text(master=frm, height=output_lines, width=103)
        output.config(state=tk.DISABLED)
        output.pack(fill=tk.X)
        return frm, output

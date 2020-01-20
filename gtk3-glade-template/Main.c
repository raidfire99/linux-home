#include <gtk/gtk.h>
GtkWidget *g_lbl_ledclr1;
int main(int argc, char *argv[])

{
    GtkBuilder      *builder; 
    GtkWidget       *window;
    gtk_init(&argc, &argv);
    builder = gtk_builder_new();
    gtk_builder_add_from_file (builder, "glade/app1.glade", NULL);
    window = GTK_WIDGET(gtk_builder_get_object(builder, "window"));
    gtk_builder_connect_signals(builder, NULL);
    

    // get pointers to the two labels
    g_lbl_ledclr1 = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_ledclr1"));
    g_object_unref(builder);
    gtk_widget_show(window);                
    gtk_main();
    return 0;

}


// called when button is clicked

void on_btn_arm_clicked()

{
  
    gtk_label_set_markup (GTK_LABEL (g_lbl_ledclr1), "<span background='green' foreground='red'>ARMED</span>");

//execlp("gnome-terminal[-e]", "hello.sh");
system ("./hello.sh");




}

// called when window is closed

void on_app1_destroy()

{

    gtk_main_quit();

}

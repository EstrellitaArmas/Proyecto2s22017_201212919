namespace Reportes
{
    partial class Reportes
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.ptbImagen = new System.Windows.Forms.Panel();
            this.ptbGrafica = new System.Windows.Forms.PictureBox();
            this.ptbImagen.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.ptbGrafica)).BeginInit();
            this.SuspendLayout();
            // 
            // ptbImagen
            // 
            this.ptbImagen.AutoScroll = true;
            this.ptbImagen.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.ptbImagen.Controls.Add(this.ptbGrafica);
            this.ptbImagen.Location = new System.Drawing.Point(30, 19);
            this.ptbImagen.Margin = new System.Windows.Forms.Padding(2);
            this.ptbImagen.Name = "ptbImagen";
            this.ptbImagen.Size = new System.Drawing.Size(886, 462);
            this.ptbImagen.TabIndex = 14;
            // 
            // ptbGrafica
            // 
            this.ptbGrafica.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ptbGrafica.Location = new System.Drawing.Point(3, 2);
            this.ptbGrafica.Margin = new System.Windows.Forms.Padding(2);
            this.ptbGrafica.Name = "ptbGrafica";
            this.ptbGrafica.Size = new System.Drawing.Size(883, 461);
            this.ptbGrafica.TabIndex = 0;
            this.ptbGrafica.TabStop = false;
            // 
            // Reportes
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(946, 500);
            this.Controls.Add(this.ptbImagen);
            this.Name = "Reportes";
            this.Text = "Reportes";
            this.ptbImagen.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.ptbGrafica)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel ptbImagen;
        private System.Windows.Forms.PictureBox ptbGrafica;
    }
}
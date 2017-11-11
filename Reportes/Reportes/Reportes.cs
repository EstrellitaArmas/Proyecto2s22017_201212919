using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Reportes
{
    public partial class Reportes : Form
    {
        public Reportes(string nombre)
        {
            InitializeComponent();
            Image img = Image.FromFile(@"C:\\Users\\estre\\Desktop\\Proyecto2s22017_201212919\\"+nombre+".jpg");
            ptbImagen.AutoScroll = true;
            ptbImagen.AutoScrollMinSize = new Size(0, 2000);
            ptbGrafica.Image = img;
            ptbGrafica.Size = new Size(2000, 2000);
        }
        

        private void ptbGrafica_Click(object sender, EventArgs e)
        {

        }
    }
}

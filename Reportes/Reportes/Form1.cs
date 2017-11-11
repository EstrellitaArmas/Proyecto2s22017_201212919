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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var path = "C:\\Users\\estre\\Desktop\\Proyecto2s22017_201212919\\Matriz";
            GenerateGraph(path);
            string matriz = "Matriz";
            Reportes dashboard = new Reportes(matriz);

            dashboard.Show();
        }

        private static void GenerateGraph(string path)
        {
            try
            {
                var command = "dot -Tjpg " + path + ".txt -o " + path + ".jpg";
                var procStartInfo = new System.Diagnostics.ProcessStartInfo("cmd", "/C " + command);
                var proc = new System.Diagnostics.Process();
                proc.StartInfo = procStartInfo;
                proc.Start();
                proc.WaitForExit();
            }
            catch (Exception x)
            {
                Console.WriteLine("ERROR EN GENERAR : " + x);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var path = "C:\\Users\\estre\\Desktop\\Proyecto2s22017_201212919\\arbolBHistorial";
            GenerateGraph(path);
            string nombre = "arbolBHistorial";
            Reportes dashboard = new Reportes(nombre);

            dashboard.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            var path = "C:\\Users\\estre\\Desktop\\Proyecto2s22017_201212919\\arbolAVLSistemaPago";
            GenerateGraph(path);
            string nombre = "arbolAVLSistemaPago";
            Reportes dashboard = new Reportes(nombre);

            dashboard.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            var path = "C:\\Users\\estre\\Desktop\\Proyecto2s22017_201212919\\listaUsuarios";
            GenerateGraph(path);
            string nombre = "listaUsuarios";
            Reportes dashboard = new Reportes(nombre);

            dashboard.Show();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            var path = "C:\\Users\\estre\\Desktop\\Proyecto2s22017_201212919\\listaHabitaciones";
            GenerateGraph(path);
            string nombre = "listaHabitaciones";
            Reportes dashboard = new Reportes(nombre);

            dashboard.Show();
        }
    }
}

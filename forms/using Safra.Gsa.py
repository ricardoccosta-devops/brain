using Safra.Gsa.WebApi;

namespace Safra.Pix.Assinatura.Mensagem
{
    public static class Program
    {
        public static void Main(string[] args)
        {
            ApiProgram.Start(args, new ProgramSetup());
        }
    }
}

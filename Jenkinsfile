def param_new = params.New_Parameter
pipeline
{
    agent any
    stages
    {
        stage('check')
        {
            steps
            {
                script
                {
                    echo "Hello Pipeline is triggered"
                    echo "The New Parameter" + param_new
                }
            }
        }
    }
}

# Histórico de Atualizações

## 30/04/2026

### 🚀 Novidades
- **Editor de Imagens**: Nova funcionalidade para editar evidências de ocorrências diretamente no sistema, com ferramentas para desenhar, recortar, girar e fazer download das imagens editadas
- **Player de Vídeo**: Adicionado suporte para visualização de vídeos na galeria de evidências
- **Ocorrências de Vendas**: Novo módulo completo para gestão de ocorrências com criação, listagem, detalhamento e conversão para pedidos
- **Promoções**: Sistema completo de gestão de promoções com operações CRUD
- **Webhook Events**: Nova funcionalidade para monitoramento e gestão de eventos webhook
- **Lista de Preços**: Implementadas operações em lote como aplicar markup por categoria, remover itens e duplicar listas
- **Relatório de Perdas**: Novo relatório disponível para análise de produtos com perdas
- **SMS para NFC-e**: Envio automático de link para download da NFC-e via SMS

### ✨ Melhorias
- **Dashboard**: Gráficos aprimorados com tooltips e legendas mais informativos, além de controle de acesso baseado em permissões
- **Inventário**: Adicionada opção para zerar quantidades de produtos não conferidos e seleção de dias do último inventário
- **Notificações**: Implementadas ações em lote para marcar como lidas e remover notificações
- **Etiquetas**: Melhorias na funcionalidade de impressão com validação aprimorada
- **Exportação de Dados**: Sistema configurável para exportação de dados implementado
- **Upload de Arquivos**: Configuração aprimorada com suporte a diferentes tipos de arquivos

### 🐛 Correções
- **Dashboard**: Corrigido tratamento de valores nulos em gráficos
- **Ocorrências**: Corrigidos problemas de fuso horário em datas e prevenção de duplo salvamento
- **Planograma**: Corrigidos problemas de mapeamento de campos
- **Sistema**: Melhorias gerais de estabilidade e performance

## 22/04/2026

### ✨ Melhorias
- **Produtos**: Otimizada lógica de mapeamento GTIN para melhor performance
- **Terminal e Planograma**: Aprimoradas opções de filtro na interface

## 20/04/2026

### 🚀 Novidades
- **Ocorrências de Vendas**: Implementado sistema completo de gestão com funcionalidades de soft-delete e histórico
- **Múltiplos GTINs**: Produtos agora suportam múltiplos códigos GTIN para maior flexibilidade
- **Validação GTIN**: Nova validação para códigos GTIN em NF-e

### ✨ Melhorias
- **Planograma**: Melhorias na funcionalidade de etiquetas com novos filtros
- **PDV**: Aprimoramentos nos filtros e seleções

### 🐛 Correções
- **Busca**: Corrigidos caracteres especiais em pesquisas
- **Comentários**: Validação aprimorada para conteúdo não vazio
- **Sistema**: Melhor tratamento de erros e logs mais informativos

## 11/04/2026

### ✨ Melhorias
- **Planograma**: Melhorias na interface e funcionalidades de etiquetagem
- **Sistema**: Aprimoramentos gerais de performance e estabilidade

## 08/04/2026

### ✨ Melhorias
- **PDV**: Melhorias no mapeamento e nomenclatura de métodos
- **Sistema**: Atualização de dependências e otimizações gerais

## 08/04/2026

🐛 **Correções**
- Melhorada a sincronização de dados do painel administrativo e inventário

## 26/03/2026

🚀 **Novidades**
- Sistema completo de gestão de promoções no painel administrativo

🐛 **Correções**
- Aprimorada a lógica de criação de usuários
- Corrigido o login com Apple

## 25/03/2026

🚀 **Novidades**
- Funcionalidade de transferência entre estoques
- Nova opção para excluir contas de clientes

🐛 **Correções**
- Melhoradas as interfaces de gestão de inventário
- Corrigido o sistema de emissão de notas fiscais para vendas de clientes

## 23/03/2026

🚀 **Novidades**
- Sistema completo de emissão de NFC-e (Nota Fiscal do Consumidor Eletrônica)
- Novos modais e funcionalidades de relatórios de inventário

🐛 **Correções**
- Melhorado o sistema de geração de relatórios

## 20/03/2026

🚀 **Novidades**
- Busca de estabelecimentos por localização (coordenadas GPS)
- Mapeamento de unidades de conversão para produtos
- Funcionalidades de aprovação e cancelamento em lote para compras
- Filtros por categoria nas entradas de estoque

🛠️ **Melhorias**
- Funcionalidade de exclusão em lote para itens do sistema
- Melhorado o sistema de atualização de datas

## 20/03/2026

🚀 **Novidades**
- Nova funcionalidade de histórico de preços dos produtos para acompanhar variações ao longo do tempo
- Suporte para conversão entre diferentes unidades de medida dos produtos
- Filtros por coordenadas geográficas para pontos de venda

✨ **Melhorias**
- Aprimoramento no gerenciamento de inventário com novos componentes visuais
- Melhorias na aprovação e cancelamento de compras em lote
- Otimização dos filtros de entrada de produtos no estoque

## 19/03/2026

🚀 **Novidades**
- Sistema completo de histórico de preços implementado para melhor controle de custos

## 13/03/2026

🐛 **Correções**
- Corrigidos problemas de layout e funcionamento na página de verificação de inventário
- Removida obrigatoriedade da data de fabricação para lotes no inventário

✨ **Melhorias**
- Atualizações na API do cliente e melhorias na organização dos dados
- Filtros de tarefas de inventário agora permitem busca por nome do inventário

## 09/03/2026

✨ **Melhorias**
- Nova funcionalidade de exportação reformulada para melhor performance

🐛 **Correções**
- Correções na normalização de códigos NCM, CEST e CFOP
- Atualização nas credenciais de autenticação OAuth do Google e Apple
- Corrigido problema de entrada duplicada no planograma

## 07/03/2026

🐛 **Correções**
- Correção na exibição de imagens públicas no painel principal

🚀 **Novidades**
- Melhorias nas sugestões de compra com filtros por termo de busca
- Suporte para múltiplos IDs de produtos nas sugestões

## 04/03/2026

✨ **Melhorias**
- Otimização nas consultas de especificações de inventário
- Atualizações nos tipos de dados para campos de observações e tags
- Melhorias nos filtros de data para pedidos de venda

## 02/03/2026

🚀 **Novidades**
- Nova página inicial redesenhada com seções de boas-vindas, guia de configuração e notícias
- Implementado sistema de histórico de mudanças (changelog) na página "Sobre"
- Adicionada área do gestor com funcionalidades específicas de administração
- Nova funcionalidade de gerenciamento de assinaturas e planos
- Sistema de filtros avançados para diversos módulos (NFe, inventário, financeiro)

✨ **Melhorias**
- Aprimoramento na geração de sugestões de compra com análise detalhada do inventário
- Interface melhorada para gerenciamento de itens NFCe
- Novos relatórios detalhados de fornecimento
- Melhorias na autenticação e interface do usuário

🐛 **Correções**
- Correções na exibição de status em modais de detalhes
- Ajustes nos filtros de pagamentos sem data de registro
- Correções nos caminhos de importação e renderização condicional de componentes

## 25/02/2026

🚀 **Novidades**
- Lançamento da área do gestor com ferramentas exclusivas de gestão
- Melhorias na recuperação de produtos com filtros por quantidade disponível e ponto de venda

## 23/02/2026

🐛 **Correções**
- Correções na navegação por abas de status
- Ajustes nos caminhos de importação de componentes
- Correções pontuais de funcionamento em diversas telas

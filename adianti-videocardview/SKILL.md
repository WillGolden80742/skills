---
name: adianti-videocardview
description: Video Cards — Tutor Presentation > Utilities > Video Cards
triggers: ["VideoCardView", "Video", "Cards", "Tutor", "Presentation", "Utilities", "Video Cards"]
---

# Skill Adianti — Video Cards — Tutor Presentation > Utilities > Video Cards

Classe Tutor: `VideoCardView`.
Ver no Tutor: `index.php?class=VideoCardView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/VideoCardView.class.php`.


## Código

```php
<?php
/**
 * VideoCardView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class VideoCardView extends TPage
{
	private $form;
	
	public function __construct()
	{
		parent::__construct();
		
		$cards = new TCardView;
		$cards->setUseButton();
		$items = [];
		$items[] = (object) [ 'id' => 1, 'title' => 'Melhorias do Framework 8.0 (2024)', 'source' => 'YEZaF9uixjY'];
		$items[] = (object) [ 'id' => 1, 'title' => 'Melhorias do Framework 7.6 (2023)', 'source' => '2ljKQpLw6WQ'];
		$items[] = (object) [ 'id' => 2, 'title' => 'Melhorias do Framework 7.5 (2022)', 'source' => 'DbFFZM1NND4'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 7.4 (2021)', 'source' => '8REC_4pQAh8'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 7.3 (2020)', 'source' => 'LXhKV2JAhss'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 7.2 (2020)', 'source' => 'EZceO7GynBw'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 7.0 (2019)', 'source' => 'YtFqNFXhnTU'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 5.5 (2018)', 'source' => 'HnC0gg1ik8o'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 5.0 (2017)', 'source' => 'IF5f1cnGl04'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 4.0 (2016)', 'source' => 'ZmLtJUpoJgk'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 3.0 (2015)', 'source' => 'TNbzKO1khcs'];
		$items[] = (object) [ 'id' => 3, 'title' => 'Melhorias do Framework 2.0 (2015)', 'source' => 'VEBwvBxBq88'];
		
		foreach ($items as $key => $item)
		{
			$cards->addItem($item);
		}
		
		$cards->setTitleAttribute('title');
		
		$cards->setItemTemplate('<iframe width="100%" height="300px" src="https://www.youtube.com/embed/{source}"></iframe>');
		
		$action = new TAction([$this, 'onGotoVideo'], ['source'=>'{source}']);
		$cards->addAction($action, 'Go to Youtube', 'far:play-circle red');
		
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($cards);

        parent::add($vbox);
	}
    
    /**
     * Item edit action
     */
	public static function onGotoVideo($param = NULL)
	{
	    $source = $param['source'];
		TScript::create("window.open('https://www.youtube.com/watch?v={$source}')");
	}
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.

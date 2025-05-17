# Gera documentação (pydoc)
doc-gen:
	pydoc -w app
	mv app.html docs/

# Exporta requisitos pip
requirements:
	pip freeze > requirements.txt
	echo "✅ requirements.txt atualizado."

# Exporta ambiente Conda resumo
env-history:
	conda env export --from-history > environment.yml
	echo "✅ environment.yml (histórico) atualizado."

# Target doc que roda tudo junto
doc: doc-gen requirements env-history
	echo "✅ Documentação e arquivos de ambiente atualizados."

run: 
	python app.py
	echo "✅ Rodando..."